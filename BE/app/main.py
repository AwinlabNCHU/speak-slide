from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .database import engine, Base, init_db
from .config import settings
from .api.v1.endpoints import auth
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize database
try:
    init_db()
    logger.info("Database initialized successfully")
except Exception as e:
    logger.error(f"Error initializing database: {str(e)}")
    raise

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Backend API for Vute application",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=False,  # Must be False when allow_origins is ["*"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])

@app.get("/")
async def root():
    return JSONResponse(
        content={
            "message": f"Welcome to {settings.PROJECT_NAME} API",
            "status": "active"
        }
    )

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    try:
        # You can add more health checks here
        return {
            "status": "ok",
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0"
        }
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Health check failed"
        )
