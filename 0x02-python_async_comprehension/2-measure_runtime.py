#!/usr/bin/env python3
"""
 parallel comprehensions
"""

import asyncio
from time import perf_counter
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the total runtime and return it
    """
    counter = perf_counter()
    asy_task = [asyncio.create_task(async_comprehension()) for i in range(4)]
    await asyncio.gather(*asy_task)
    return perf_counter() - counter
