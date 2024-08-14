#!/usr/bin/env python3
"""
Module: Request caching and tracking tools
"""
import redis
import requests
from functools import wraps
from typing import Callable, Any, List, Dict


redis_store = redis.Redis(host='localhost', port=6379, db=0)
'''The module-level Redis instance.
'''


def data_cacher(ttl: int = 10) -> Callable:
    """
    Caches the output of fetched data for a specified TTL.
    """
    def decorator(method: Callable) -> Callable:
        @wraps(method)
        def invoker(url: str) -> str:
            """
            The wrapper function for caching the output.
            """
            redis_store.incr(f'count:{url}')
            result = redis_store.get(f'result:{url}')
            if result:
                return result.decode('utf-8')
            result = method(url)
            redis_store.setex(f'result:{url}', ttl, result)
            return result
        return invoker
    return decorator


@data_cacher(ttl=10)
def get_page(url: str) -> str:
    """
    Returns content of URL after caching request's
    response, and tracking request.
    """
    return requests.get(url).text


if __name__ == '__main__':
    print(get_page('https://www.example.com'))
