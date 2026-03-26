from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.db import db

app = FastAPI(title="Backend", version="1.0.0")


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(api_router, prefix="/api/v1")