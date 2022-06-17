#!/usr/bin/env python3
''' import async_generator from the previous task and then
    write a coroutine called async_comprehension that takes
    no arguments
'''
from typing import List
vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> vector:
    ''' func will collect 10 random numbers using an async
        comprehensing over async_generator, then return the 10
        random numbers
    '''
    final = [y async for y in async_generator()]
    return final
