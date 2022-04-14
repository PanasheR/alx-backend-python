#!/usr/bin/env python3
""" multiplying floats """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ functions multiplies floats """
    def fun(num: float):
        return num * multiplier
    return fun
