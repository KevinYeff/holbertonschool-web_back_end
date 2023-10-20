#!/usr/bin/env python3
"""Task 5 complex types - list of floats"""


def sum_list(input_list: list) -> float:
    """A type-annotated function that takes a list
    of floats as argument and returns their sum as
    a float"""
    sum = 0
    for float in input_list:
        sum += float
    return sum
