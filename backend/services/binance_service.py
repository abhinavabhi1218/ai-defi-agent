import httpx
from backend.core.redis_client import redis_client

BINANCE_URL = "https://api.binance.com/api/v3/ticker/price"


async def get_symbol_price(symbol: str):

    # Try Redis cache first
    try:
        cached_price = await redis_client.get(symbol)

        if cached_price:
            return {
                "symbol": symbol,
                "price": float(cached_price),
                "source": "cache"
            }
    except Exception:
        pass  # Redis failure should not break API

    # Fetch from Binance
    url = f"{BINANCE_URL}?symbol={symbol}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    data = response.json()
    price = float(data["price"])

    # Store in Redis with TTL
    try:
        await redis_client.set(symbol, price, ex=2)
    except Exception:
        pass

    return {
        "symbol": symbol,
        "price": price,
        "source": "binance"
    }