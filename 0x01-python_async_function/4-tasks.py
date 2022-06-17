#!/usr/bin/env python3
''' Take the code from wait_n and alter it into a new
    function task_wait_n. The code is nearly identical
    to wait_n except task_wait_random is being called.
'''
import asyncio
from typing import List

get = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Func repeats task 3
    '''
    a = [get(max_delay) for i in range(n)]
    fnsh = [await task for task in asyncio.as_completed(a)]
    return fnsh
