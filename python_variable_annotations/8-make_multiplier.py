#!/usr/bin/env python3
"""Task 8 Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A type-annotated function that takes a float as argument
    and returns a function that multiplies a float"""
    def function(num: float):
        """Function that multiplies a float number by the
        argument of the previous function"""
        return num * multiplier
    return function
