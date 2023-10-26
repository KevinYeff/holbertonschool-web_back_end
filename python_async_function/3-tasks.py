#!/usr/bin/env python3
"""Task 3: Tasks"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that takes an int as an argument and returns
    an async task"""
    # creating a task using a coroutine (wait_random)
    task = asyncio.create_task(wait_random(max_delay))
    return task
