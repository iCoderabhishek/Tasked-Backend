from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserLogin, UserResponse, TokenResponse
from app.services.auth_service import register_user, login_user

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def register(data: UserCreate) -> UserResponse:
    try:
        user = await register_user(data)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenResponse)
async def login(data: UserLogin) -> TokenResponse:
    try:
        user = await login_user(data)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))