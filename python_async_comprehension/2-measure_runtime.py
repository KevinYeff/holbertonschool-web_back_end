#!/usr/bin/env python3
"""Task 2 Run time for four parallel comprehensions"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of the coroutine function
    async_comprehension that it's executed 4 times in parallel"""
    # initial time
    start = time()
    # uses an async comprehensing over async_comprehension
    # calls the coroutine 4 times in parallel
    cours = [async_comprehension() for i in range(4)]
    # uses gather to execute the coroutines
    # and waits for the tasks to be completed in parallel
    await asyncio.gather(*cours)
    # ending
    end = time()
    return end - start
