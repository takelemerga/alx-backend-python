#!/usr/bin/env python3
"""
module
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ 
    return length of a list of sequences
    """
    return [(i, len(i)) for i in lst]
