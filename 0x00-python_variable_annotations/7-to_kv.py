#!/usr/bin/env python3
"""
function module

"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts variable to a Key value pairs"""
    return k, v ** 2
