#!/usr/bin/env python3
""" float sum of ints and floats """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ function returns float sum for ints and float """
    return sum(mxd_lst)
