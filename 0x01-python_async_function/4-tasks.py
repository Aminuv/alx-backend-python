#!/usr/bin/env python3
"""  The code is nearly identical to wait_n except task_wait_random """
import asyncio
from typing import List

tasks_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ function  being called """
    w_time = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(w_time)
