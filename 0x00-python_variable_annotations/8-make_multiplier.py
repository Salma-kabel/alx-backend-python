#!/usr/bin/env python3
"""function make_multiplier that takes a
float multiplier as argument """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """that takes a float multiplier as argument and returns a
    function that multiplies a float by multiplier"""
    def multiply(number: float) -> float:
        return number * multiplier
    return multiply
