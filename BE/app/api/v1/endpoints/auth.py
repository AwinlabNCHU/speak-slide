from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Any
from ....core.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user,
    generate_temporary_password
)
from ....core.email import send_password_reset_email
from ....schemas import UserCreate, UserResponse, Token
from ....models.user import User
from ....database import get_db
import logging
from pydantic import BaseModel

# Set up logging
logger = logging.getLogger(__name__)

router = APIRouter()

class ForgotPasswordRequest(BaseModel):
    email: str

class LoginRequest(BaseModel):
    email: str
    password: str

@router.get("/debug/user/{email}")
def debug_user(email: str, db: Session = Depends(get_db)):
    """
    Debug endpoint to check if a user exists and their details.
    """
    logger.info(f"Checking user existence for email: {email}")
    user = db.query(User).filter(User.email == email).first()
    if not user:
        logger.info(f"User not found for email: {email}")
        return {"exists": False, "message": "User not found"}
    logger.info(f"User found: {user.email}")
    return {
        "exists": True,
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "is_active": user.is_active,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        }
    }

@router.post("/register", response_model=UserResponse)
def register(*, db: Session = Depends(get_db), user_in: UserCreate) -> Any:
    """
    Register a new user.
    """
    logger.info(f"Attempting to register user with email: {user_in.email}")
    
    # Check if user with email exists
    user = db.query(User).filter(User.email == user_in.email).first()
    if user:
        logger.warning(f"User with email {user_in.email} already exists")
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    
    # Check if user with username exists
    user = db.query(User).filter(User.username == user_in.username).first()
    if user:
        logger.warning(f"User with username {user_in.username} already exists")
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    
    # Create new user
    try:
        user = User(
            email=user_in.email,
            username=user_in.username,
            full_name=user_in.full_name,
            hashed_password=get_password_hash(user_in.password),
            is_active=user_in.is_active
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        logger.info(f"Successfully registered user: {user.email}")
        return user
    except Exception as e:
        logger.error(f"Error registering user: {str(e)}")
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Error creating user"
        )

@router.post("/login", response_model=Token)
def login(login_data: LoginRequest, db: Session = Depends(get_db)) -> Any:
    """
    Login using email and password, get an access token for future requests.
    """
    logger.info(f"Login attempt for email: {login_data.email}")
    user = db.query(User).filter(User.email == login_data.email).first()
    if not user:
        logger.warning(f"Login failed: User not found for email {login_data.email}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not verify_password(login_data.password, user.hashed_password):
        logger.warning(f"Login failed: Incorrect password for user {user.email}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_active:
        logger.warning(f"Login failed: Inactive user {user.email}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    access_token = create_access_token(subject=user.id)
    logger.info(f"Login successful for user: {user.email}")
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.post("/forgot-password")
async def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)) -> Any:
    """
    Send a temporary password to the user's email.
    """
    logger.info(f"Forgot password request for email: {request.email}")
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        logger.warning(f"Forgot password failed: User not found for email {request.email}")
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    temporary_password = generate_temporary_password()
    user.hashed_password = get_password_hash(temporary_password)
    db.add(user)
    db.commit()
    
    await send_password_reset_email(request.email, temporary_password)
    logger.info(f"Temporary password sent to: {request.email}")
    return {"message": "Temporary password has been sent to your email"}

@router.post("/reset-password")
def reset_password(
    current_password: str,
    new_password: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Reset password for logged in user.
    """
    logger.info(f"Password reset attempt for user: {current_user.email}")
    if not verify_password(current_password, current_user.hashed_password):
        logger.warning(f"Password reset failed: Incorrect current password for user {current_user.email}")
        raise HTTPException(
            status_code=400,
            detail="Incorrect password"
        )
    
    current_user.hashed_password = get_password_hash(new_password)
    db.add(current_user)
    db.commit()
    logger.info(f"Password reset successful for user: {current_user.email}")
    return {"message": "Password updated successfully"} 