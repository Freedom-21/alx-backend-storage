#!/usr/bin/env python3
"""web"""

import requests
import redis

r = redis.Redis()


def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL and cache it.
    """
    key = f"count:{url}"
    r.incr(key)
    cached_content = r.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    response = requests.get(url)
    r.setex(url, 10, response.text)
    return response.text
