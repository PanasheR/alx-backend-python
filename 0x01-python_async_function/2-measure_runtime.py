#!/usr/bin/env python3
''' measures the total execution time '''
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''  function should return a float '''
    fst = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    fnsh = time.perf_counter()
    sum_time = fnsh - fst
    return sum_time / n
