#!/usr/bin/env python3
"""Task 10 Duc typing - first element of a sequence"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns an element if there is any otherwise returns none"""
    if lst:
        return lst[0]
    else:
        return None
