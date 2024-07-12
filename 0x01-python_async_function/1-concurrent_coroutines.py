#!/usr/bin/env python3
"""routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


time = [wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
