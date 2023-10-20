#!/usr/bin/env python3
"""Task 6 Complex types - mixed list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A type-annotated function that takes a list of ints and floats
    and returns their sum as a float"""
    sum: float = 0.0
    for nums in mxd_lst:
        sum += nums
    return sum
