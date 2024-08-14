#!/usr/bin/env python3
"""
web cach and tracker
"""
import requests
import time
from functools import wraps

cache = {}

def cache_result(ttl=10):  # 10 seconds default TTL
    def decorator(func):
        def wrapper(url):
            cache_key = f"result:{url}"
            count_key = f"count:{url}"
            if cache_key in cache and time.time() - cache[cache_key][0] < ttl:
                return cache[cache_key][1]
            result = func(url)
            cache[cache_key] = (time.time(), result)
            cache[count_key] = cache.get(count_key, 0) + 1
            return result
        return wrapper
    return decorator

@cache_result()
def get_page(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text

# Example usage:
print(get_page("http://slowwly.robertomurray.co.uk"))
print(get_page("http://slowwly.robertomurray.co.uk"))
print(cache["count:http://slowwly.robertomurray.co.uk"])
