#!/usr/bin/env python3
"""Task 0 Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that helps to get the range of indexes
    Parameters:
     @page: integer
     @page_size: integer
    Return: A tuple containing the range of indexes from
    start to end
    Note: In Pagination all the indexes starts at 1"""
    if page > 0 and page_size > 0:
        pass
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
