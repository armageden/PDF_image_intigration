"""
Application configuration using pydantic-settings
Loads from environment variables with validation
"""

from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Application
    APP_NAME: str = "PDF-to-Image Illustration API"
    DEBUG: bool = False
    SECRET_KEY: str = "change-me-in-production-use-secrets-token-hex-32"
    
    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./data/app.db"
    
    # JWT Configuration
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]
    
    # File Upload
    MAX_UPLOAD_SIZE: int = 50 * 1024 * 1024  # 50MB
    UPLOAD_DIR: str = "uploads"
    GENERATED_DIR: str = "generated"
    ALLOWED_EXTENSIONS: List[str] = [".pdf"]
    
    # AI Image Generation
    AI_API_KEY: str = ""
    AI_API_URL: str = "https://api.openai.com/v1/images/generations"
    AI_MODEL: str = "dall-e-3"
    
    # Rate Limiting
    RATE_LIMIT_AUTH: str = "5/minute"
    RATE_LIMIT_UPLOAD: str = "10/hour"
    RATE_LIMIT_GENERATE: str = "20/hour"
    RATE_LIMIT_GENERAL: str = "100/minute"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Global settings instance
settings = Settings()


def get_database_url() -> str:
    """Get database URL, ensuring data directory exists"""
    if settings.DATABASE_URL.startswith("sqlite"):
        # Extract path from SQLite URL and ensure directory exists
        db_path = settings.DATABASE_URL.split("///")[-1]
        db_dir = os.path.dirname(db_path)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)
    return settings.DATABASE_URL
