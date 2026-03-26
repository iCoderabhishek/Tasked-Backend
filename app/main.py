from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(title="Backend", version="1.0.0")

@app.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api/v1")
