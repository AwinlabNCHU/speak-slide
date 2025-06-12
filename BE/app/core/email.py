from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from ..config import settings
from typing import List
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Check if email configuration is available
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_FROM = os.getenv("MAIL_FROM")
MAIL_PORT = int(os.getenv("MAIL_PORT", "587"))
MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")

# Check if email service is configured
is_email_configured = all([MAIL_USERNAME, MAIL_PASSWORD, MAIL_FROM])

if is_email_configured:
    logger.info("Email service is configured")
    conf = ConnectionConfig(
        MAIL_USERNAME=MAIL_USERNAME,
        MAIL_PASSWORD=MAIL_PASSWORD,
        MAIL_FROM=MAIL_FROM,
        MAIL_PORT=MAIL_PORT,
        MAIL_SERVER=MAIL_SERVER,
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False,
        USE_CREDENTIALS=True
    )
    fastmail = FastMail(conf)
else:
    logger.warning("Email service is not configured. Password reset emails will be logged instead of sent.")
    fastmail = None

async def send_password_reset_email(email_to: str, temporary_password: str):
    """
    Send a password reset email with a temporary password.
    If email service is not configured, log the temporary password instead.
    """
    try:
        if not is_email_configured:
            logger.info(f"Email service not configured. Temporary password for {email_to}: {temporary_password}")
            return True

        message = MessageSchema(
            subject="Password Reset Request",
            recipients=[email_to],
            body=f"Your temporary password is: {temporary_password}\nPlease change your password after logging in.",
            subtype="html"
        )
        
        await fastmail.send_message(message)
        logger.info(f"Password reset email sent to {email_to}")
        return True
    except Exception as e:
        logger.error(f"Error sending password reset email: {str(e)}")
        return False 