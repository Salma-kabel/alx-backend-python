#!/usr/bin/env python3
"""coroutine called async_comprehension that takes no arguments"""


from typing import List
from random import uniform
import asyncio


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """will collect 10 random numbers using an async comprehensing over
    async_generator, then return the 10 random numbers"""
    res = [await i async for i in async_generator()]
    return res
