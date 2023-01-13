from fastapi import FastAPI
from src.app.routes.routes import router

app = FastAPI()

app.include_router(router, prefix="/warehouse_items", tags=["warehouse_item"])
