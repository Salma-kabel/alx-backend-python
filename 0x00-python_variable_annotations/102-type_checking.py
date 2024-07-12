#!/usr/bin/env python3
"""validate the following piece of code"""


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """validate the following piece of code
    and apply any necessary changes"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
