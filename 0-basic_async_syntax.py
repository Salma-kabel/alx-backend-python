#!/usr/bin/env python3
"""coroutine that takes in an integer argument (max_delay,
with a default value of 10) named wait_random"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay
    (inclusive and float value) seconds and eventually returns it"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
