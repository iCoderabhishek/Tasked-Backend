from fastapi import APIRouter, Depends
from typing import List
from app.core.dependencies import get_current_user
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services import task_service

router = APIRouter()

@router.post("/", response_model=TaskResponse)
async def create_task(data: TaskCreate, user = Depends(get_current_user)):
    return await task_service.create_task(data, user)

@router.get("/", response_model=List[TaskResponse])
async def get_tasks(user = Depends(get_current_user)):
    return await task_service.get_tasks(user)

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, user = Depends(get_current_user)):
    return await task_service.get_task(task_id, user)

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, data: TaskUpdate, user = Depends(get_current_user)):
    return await task_service.update_task(task_id, data, user)

@router.delete("/{task_id}")
async def delete_task(task_id: int, user = Depends(get_current_user)):
    return await task_service.delete_task(task_id, user)