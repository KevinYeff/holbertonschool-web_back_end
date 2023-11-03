#!/usr/bin/env python3
"""Task 0 Async Generator"""

import asyncio
from typing import Generator
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """Coroutine function that takes no arguments
    The coroutine will loop 10 times, each time
    asynchronously wait 1 second, the yield a random
    number between 0 and 10
    Generates: float numbers"""
    for i in range(10):
        # 2nd iteration Reanudes
        # waits 1 sec per iteration
        await asyncio.sleep(1)
        # generates a random float number on demand
        yield uniform(0, 10)
        # 1st iteration Pauses
