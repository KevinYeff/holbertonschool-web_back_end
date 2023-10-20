#!/usr/bin/env python3
"""Task 7 Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A type-annotated function that takes a string and a
    int/float as argments and returns a tuple
    the k argument is always a string
    the v argument is the square of the int/float"""
    return k, v*v
