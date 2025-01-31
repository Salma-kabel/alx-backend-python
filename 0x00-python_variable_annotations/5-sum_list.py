#!/usr/bin/env python3
"""function sum_list which takes a list input_list
of floats as argument"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list input_list of floats as argument
    and returns their sum as a float"""
    total = 0.0
    for number in input_list:
        total += number
    return total
