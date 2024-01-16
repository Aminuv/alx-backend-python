#!/usr/bin/env python3
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ def function """
    str_time = time.pref_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.pref_counter()
    return (end_time - str_time) / n
