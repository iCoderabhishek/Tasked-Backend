from app.core.db import db
from app.core.security import hash_password, verify_password, create_access_token


async def register_user(data):
    existing_user = await db.user.find_unique(where={"email": data.email})
    if existing_user:
        raise Exception("User already exists")

    print("PASSWORD:", data.password, len(data.password))
    print("PASSWORD:", data.password)
    print("LENGTH:", len(data.password.encode()))
    user = await db.user.create(
        data={
            "email": data.email,
            "password": hash_password(data.password),
        }
    )

    return user


async def login_user(data):
    user = await db.user.find_unique(where={"email": data.email})
    if not user:
        raise Exception("Invalid credentials")

    if not verify_password(data.password, user.password):
        raise Exception("Invalid credentials")

    token = create_access_token({"user_id": user.id, "role": user.role})

    return {"access_token": token, "token_type": "bearer"}

async def get_all_users():
    return await db.user.find_many()

async def delete_user(user_id: int):
    user = await db.user.find_unique(where={"id": user_id})
    if not user:
        raise Exception("User not found")
    await db.user.delete(where={"id": user_id})
    return {"message": "User deleted successfully"}