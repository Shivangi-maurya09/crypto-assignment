import ccxt
from utils.cache import cache_data, get_cached


def get_historical_data(symbol="BTC"):
    try:
        exchange = ccxt.binance()
        # CCXT wants BTC/USDT format
        pair = symbol.upper() + "/USDT"

        # Fetch 1-day historical OHLCV (open, high, low, close, volume)
        candles = exchange.fetch_ohlcv(pair, timeframe="1h", limit=24)

        data = []
        for candle in candles:
            data.append({
                "timestamp": candle[0],
                "open": candle[1],
                "high": candle[2],
                "low": candle[3],
                "close": candle[4]
            })

        return data

    except Exception as e:
        return {"error": str(e)}
