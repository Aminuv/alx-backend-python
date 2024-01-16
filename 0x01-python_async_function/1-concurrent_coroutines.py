#!/usr/bin/env python3
""" spaw wait_tme n times with the specified max_delay. """
import asyncio

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ def Function """
    w_time = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(w_time)
