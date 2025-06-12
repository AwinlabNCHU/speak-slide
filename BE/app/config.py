from pydantic_settings import BaseSettings
from functools import lru_cache
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Vute"

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./vute.db")

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:8000",
        "http://localhost:5173",
        "https://speak-slide-be.onrender.com",
        "https://speak-slide.onrender.com",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:3000",
        "https://awinlabnchu.github.io"  # GitHub Pages frontend
    ]

    class Config:
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
