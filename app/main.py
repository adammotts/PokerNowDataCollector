from fastapi import FastAPI
from app.routes.items import router as items_router
from app.routes.health import router as health_router

app = FastAPI()

app.include_router(items_router, prefix="/items")
app.include_router(health_router, prefix="/health")