from fastapi import FastAPI
from backend.routers.price_router import router as price_router

app = FastAPI()

app.include_router(price_router)