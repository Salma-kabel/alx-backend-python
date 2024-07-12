#!/usr/bin/env python3
""" nearly identical to wait_n except task_wait_random is being called"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """like wait_n except task_wait_random is being called""" 
    delay: List = []

    for i in range(n):
        delay.append(task_wait_random(max_delay))

    new_list: List[float] = []

    for dely in asyncio.as_completed(delays):
        done: float = await dely
        list2.append(done)

    return list2
