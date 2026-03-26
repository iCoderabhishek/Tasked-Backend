from fastapi import APIRouter

router = APIRouter()

@router.get("/")

def test_auth() -> dict:
    return {"message": "auth works"}