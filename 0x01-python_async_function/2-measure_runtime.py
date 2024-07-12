#!/usr/bin/env python3
"""function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay)"""


import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for
    wait_n(n, max_delay), and returns total_time / n"""
    begin = time.time()
    wait_n(n, max_delay)
    end = time.time()
    total = end - begin
    avrg = total / n
    return avrg
