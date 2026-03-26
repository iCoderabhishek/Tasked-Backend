from fastapi import APIRouter

router = APIRouter()

@router.get("/")

def test_tasks():
    return {"message": "tasks works"}