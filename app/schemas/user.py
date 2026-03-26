from pydantic import BaseModel, EmailStr, Field, field_validator
import re


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=20)

    @field_validator("password")
    def validate_password(cls, v):
        if not re.search(r"[A-Za-z]", v):
            raise ValueError("Must include a letter")
        if not re.search(r"\d", v):
            raise ValueError("Must include a number")
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=20)


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str



class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"