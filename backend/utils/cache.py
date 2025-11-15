from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=60)

def cache_data(key, value):
    cache[key] = value

def get_cached(key):
    return cache.get(key, None)
