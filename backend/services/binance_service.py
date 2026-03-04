import httpx

async def get_price(symbol: str):

    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    return response.json()