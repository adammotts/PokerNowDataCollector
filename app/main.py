from fastapi import FastAPI
from app.routes.data import router as data_router
from app.routes.health import router as health_router

app = FastAPI()

app.include_router(data_router, prefix="/data")
app.include_router(health_router, prefix="/health")