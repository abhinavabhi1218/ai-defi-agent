from fastapi import APIRouter
from backend.services.binance_service import get_price

router = APIRouter()

@router.get("/price/{symbol}")
async def price(symbol: str):
    return await get_price(symbol)