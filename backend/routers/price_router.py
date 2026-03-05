from fastapi import APIRouter
from backend.services.binance_service import get_symbol_price

router = APIRouter()

@router.get("/price/{symbol}")
async def get_price(symbol: str):
    return await get_symbol_price(symbol)