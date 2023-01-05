#!/usr/bin/env python3
"""
function module

"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float  as argument and
    returns a function that multiplies a float by multiplier.
    """
    return lambda k: k * multiplier
