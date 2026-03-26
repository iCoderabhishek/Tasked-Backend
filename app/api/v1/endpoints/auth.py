from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.user import UserCreate, UserLogin, UserResponse, TokenResponse
from app.services.auth_service import register_user, login_user, get_all_users, delete_user
from app.core.dependencies import get_current_user, get_current_admin_user

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


@router.get("/me")
async def get_me(user = Depends(get_current_user)):
    return {
        "id": user.id,
        "email": user.email,
        "role": user.role
    }


@router.get("/admin/me")
async def get_admin_me(user = Depends(get_current_admin_user)):
    return {
        "id": user.id,
        "email": user.email,
        "role": user.role
    }

@router.get("/admin/users", response_model=List[UserResponse])
async def list_users(user = Depends(get_current_admin_user)):
    try:
        users = await get_all_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/admin/users/{user_id}")
async def remove_user(user_id: int, user = Depends(get_current_admin_user)):
    try:
        return await delete_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))