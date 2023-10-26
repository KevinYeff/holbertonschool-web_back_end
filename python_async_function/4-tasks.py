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
    delays_of_prev_func: List[float] = []
    for i in range(n):
        # we are going to store all the delays provided by the
        # previous function n times
        delay_obtained = task_wait_random(max_delay)
        delays_of_prev_func.append(delay_obtained)
    # at this point every number generated by the prev function
    # is unsorted, the reason is that the current n time not always
    # be less than the next n time
    # let's define a list
    final_delay_list_sorted: List[float] = []
    # we need to sort the results of the prev function
    for current_task in asyncio.as_completed(delays_of_prev_func):
        # At this point the asyncio.as_completed function returns a
        # future sequence in ascending order but we can't save them
        # for current_task take this as the current iterable, so it needs
        # to finalice to go to the next task
        task_to_save = await current_task
        # once the current task is donde append it to the final list
        final_delay_list_sorted.append(task_to_save)
    # return the sorted list
    return final_delay_list_sorted
