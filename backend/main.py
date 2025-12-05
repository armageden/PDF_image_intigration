from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import os

from src.config import settings
from src.models.database import init_db
from src.api import auth, pdf, images, users
from src.middleware.security import SecurityHeadersMiddleware


# Rate limiter setup
limiter = Limiter(key_func=get_remote_address)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan - startup and shutdown events"""
    # Startup
    await init_db()
    
    # Create upload directories
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    os.makedirs(settings.GENERATED_DIR, exist_ok=True)
    
    yield
    
    # Shutdown (cleanup if needed)
    pass


# Create FastAPI application
app = FastAPI(
    title="PDF-to-Image Illustration API",
    description="Transform PDF documents into AI-generated visual illustrations",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/api/docs" if settings.DEBUG else None,
    redoc_url="/api/redoc" if settings.DEBUG else None,
)

# Add rate limiter to app state
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

# Security headers middleware
app.add_middleware(SecurityHeadersMiddleware)

# Mount static files for generated images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include API routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(pdf.router, prefix="/api/v1/pdf", tags=["PDF Processing"])
app.include_router(images.router, prefix="/api/v1/images", tags=["Image Generation"])
app.include_router(users.router, prefix="/api/v1/user", tags=["User Management"])


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy", "version": "1.0.0"}


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "PDF-to-Image Illustration API",
        "docs": "/api/docs" if settings.DEBUG else "API documentation disabled in production",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
