#!/usr/bin/env python3
''' Import wait_random from 0-basic_async_syntax '''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' func hat takes an integer max_delay and
    returns a asyncio.Task
    '''
    end = asyncio.create_task(wait_random(max_delay))
    return end
