#!/usr/bin/env python3
'''This module defines a function `measure_runtime
that measures the time of four parallel async comprehensions
'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes async_comprehension 4 times and measures the
    total execution time
    '''
    start_time = time.time()

    await asyncio.gather(*[async_comprehension() for i in range(4)])

    end_time = time.time()
    lag = end_time - start_time
    return lag
