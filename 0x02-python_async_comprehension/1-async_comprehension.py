#!/usr/bin/env python3
""" function takes no arguments """
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ List 10 Numbers """
    return [random async for random in async_comprehension()]
