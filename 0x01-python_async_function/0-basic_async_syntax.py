#!/usr/bin/env python3
""" asynchonous coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ def function. """
    w_time = random.uniform(0, max_delay)
    await asyncio.sleep(w_time)
    return w_time
