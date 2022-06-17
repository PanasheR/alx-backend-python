#!/usr/bin/env python3
""" Import wait_random from the previous python file """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Func returns list
    """
    lis = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    fnsh = [await task for task in asyncio.as_completed(lis)]
    return fnsh
