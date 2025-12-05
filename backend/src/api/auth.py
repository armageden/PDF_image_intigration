
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel, EmailStr, Field

router = APIRouter()
security = HTTPBearer()


class RegisterRequest(BaseModel):
    """Registration request schema"""
    email: EmailStr
    password: str = Field(..., min_length=12)
    name: str = Field(..., min_length=2, max_length=100)


class LoginRequest(BaseModel):
    """Login request schema"""
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """Token response schema"""
    access_token: str
    token_type: str = "bearer"
    expires_in: int


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest):
    """Register a new user account"""
    # TODO: Implement in Day 3
    return {"message": "User registration - to be implemented", "email": request.email}


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    """Authenticate user and return access token"""
    # TODO: Implement in Day 3
    return {
        "access_token": "placeholder_token",
        "token_type": "bearer",
        "expires_in": 900
    }


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token():
    """Refresh access token using refresh token cookie"""
    # TODO: Implement in Day 3
    return {
        "access_token": "placeholder_refreshed_token",
        "token_type": "bearer",
        "expires_in": 900
    }


@router.post("/logout")
async def logout():
    """Logout user and invalidate tokens"""
    # TODO: Implement in Day 3
    return {"message": "Logged out successfully"}
