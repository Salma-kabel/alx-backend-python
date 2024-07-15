#!/usr/bin/env python3
"""function sum_mixed_list which takes a list
mxd_lst of integers and floats"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list mxd_lst of integers and floats
    and returns their sum as a float"""
    total = 0.0
    for number in mxd_lst:
        total += number
    return total
