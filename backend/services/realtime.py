import requests
from utils.cache import cache_data, get_cached



API_URL = "https://api.coingecko.com/api/v3/coins/{}"

def get_crypto_price(symbol="BTC"):
    symbol = symbol.upper()

    # Check cache
    cached = get_cached(f"price-{symbol}")
    if cached:
        return cached

    # Convert BTC → bitcoin
    mapping = {
        "BTC": "bitcoin",
        "ETH": "ethereum",
        "BNB": "binancecoin",
        "SOL": "solana"
    }

    coin_id = mapping.get(symbol, "bitcoin")

    response = requests.get(API_URL.format(coin_id))

    if response.status_code != 200:
        return {"symbol": symbol, "price_usd": None, "message": "API unavailable"}

    data = response.json()

    try:
        price = data["market_data"]["current_price"]["usd"]
    except:
        return {"symbol": symbol, "price_usd": None, "message": "Price not found"}

    final = {
        "symbol": symbol,
        "price_usd": round(price, 2)
    }

    cache_data(f"price-{symbol}", final)
    return final
