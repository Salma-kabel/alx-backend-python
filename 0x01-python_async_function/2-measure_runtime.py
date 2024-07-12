#!/usr/bin/env python3
"""measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather"""


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for
    wait_n(n, max_delay), and returns total_time / n"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    avrg = total_time / n
    return avrg
