#!/usr/bin/env python3
"""measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather"""


import asyncio
from typing import List
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return it"""
    begin = time.time()
    async_comp = async_comprehension()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    runtime = end - begin
    return runtime
