#!/usr/bin/env python3
"""
asyio module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
