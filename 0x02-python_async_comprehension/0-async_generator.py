#!/usr/bin/env python3
""" function takes no arguments """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ loop 10 time asynchronously """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.unifor,(0, 10)
