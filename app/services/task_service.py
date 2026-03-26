from app.core.db import db
from fastapi import HTTPException


async def create_task(data, user):
    return await db.task.create(
        data={
            "title": data.title,
            "description": data.description,
            "userId": user.id
        }
    )


async def get_tasks(user):
    if user.role == "admin":
        return await db.task.find_many()

    return await db.task.find_many(
        where={"userId": user.id}
    )


async def get_task(task_id, user):
    task = await db.task.find_unique(where={"id": task_id})

    if not task:
        raise HTTPException(404, "Task not found")

    if user.role != "admin" and task.userId != user.id:
        raise HTTPException(403, "Not allowed")

    return task


async def update_task(task_id, data, user):
    task = await get_task(task_id, user)

    return await db.task.update(
        where={"id": task_id},
        data=data.dict(exclude_unset=True)
    )


async def delete_task(task_id, user):
    task = await get_task(task_id, user)

    await db.task.delete(where={"id": task_id})
    return {"message": "Task deleted"}