#!/usr/bin/env python3
''' Import async_comprehension from the previous file '''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Func will execute async_comprehension four times in parallel
    using asyncio.gather
    '''
    strt = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.perf_counter()
    return end - strt
