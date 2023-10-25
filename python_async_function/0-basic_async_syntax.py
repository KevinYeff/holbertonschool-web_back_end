#!/usr/bin/env python3
"""Task 0: The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronus corountine that takes in an integer argument
    and waits for a random delay between 0 and the default value
    o the argument (included and float value) seconds and
    evenually returns it"""
    # what we need to do is, find a way to generate a random
    # number between 0 and max_delay, this number will be our
    # delay timer
    delay_float_time = random.uniform(0, max_delay)
    # apply the timer and waits the time generated
    await asyncio.sleep(delay_float_time)
    # return that timer
    return delay_float_time
