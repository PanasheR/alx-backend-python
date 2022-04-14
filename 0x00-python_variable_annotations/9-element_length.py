#!/usr/bin/env python3
""" function annotations """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function for annotations """
    return [(i, len(i)) for i in lst]
