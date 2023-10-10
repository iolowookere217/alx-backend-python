#!/usr/bin/env python3
"""This module defines the function 'wait_n'
and Lets us execute multiple coroutines
at the same time with async
"""

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''return the list of all the delays as float values
    '''
    tasks = [wait_random(max_delay) for _ in range(n)]

    waits = await asyncio.gather(*tasks)

    return sorted(waits)
