#!/usr/bin/env python3
"""Task 4: Tasks"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine function that takes in 2 int arguments, the
    previous function will be spawmed n times with the specified
    max_delay.

    arguments:
        n: int
        max_delay: int

    return: A list with all the delays (float values) in ascending
    order without using sort() because of concurrency"""
    delays = [task_wait_random(max_delay) for i in range(n)]
    sorted_results = [await task for task in asyncio.as_completed(delays)]

    return sorted_results
