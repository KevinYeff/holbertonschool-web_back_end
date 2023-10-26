#!/usr/bin/env python3
"""Task 2 Measure the runtime"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function that takes 2 int as arguments and measures the total
    execution time for the previous function and returns the average
    time of the execution
    arguments:
        n: int
        max_delay: int
    return: The average time of execution of the prev function (wait_n)"""
    # We start the timer, perf_counter is a high precision and stable timer
    start = time.perf_counter()
    # wait_n is an async function so in order to be executed, it needs to be
    # specified as an async function.
    # Note that if we call the function it will bring errors, it will never be
    # awaited and if we use await on wait_n since the measure_time is a non
    # async function it will bring another error that specifies 'await'
    # outside async function
    asyncio.run(wait_n(n, max_delay))
    # end the timer
    end = time.perf_counter()
    # we need to extrac the time at the start from the end
    execution_time = end - start
    # if we divided by n it will bring us the average execution time
    return execution_time / n
