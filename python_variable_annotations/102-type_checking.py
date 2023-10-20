#!/usr/bin/env python3
"""Task 12 Type checking"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """takes a tuple as an argument and returns a list,
    in this list every element in the tuple will be repeated
    by the factor"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))


# print(zoom_2x)
# print(zoom_3x)
