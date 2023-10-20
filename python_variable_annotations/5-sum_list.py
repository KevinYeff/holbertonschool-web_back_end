#!/usr/bin/env python3
"""Task 5 complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """A type-annotated function that takes a list
    of floats as argument and returns their sum as
    a float"""
    sum: float = 0.0
    for floats in input_list:
        sum += floats
    return sum
