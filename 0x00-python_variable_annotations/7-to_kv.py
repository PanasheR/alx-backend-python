#!/usr/bin/env python3
""" string or float to turple return value """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ function converts float or string to turple """
    return (k, v * v)
