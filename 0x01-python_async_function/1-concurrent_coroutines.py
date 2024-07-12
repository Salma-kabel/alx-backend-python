#!/usr/bin/env python3
"""routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    time = [wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*time)
    return sorted(results)
