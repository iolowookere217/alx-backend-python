#!/usr/bin/env python3

"""This module defines a function
called `async_generator` that
"""

from typing import Generator
import random
import asyncio


"""float is return type of the yield
   None means the generator wont take any parameter
   None means no error will be raised
"""


async def async_generator() -> Generator[float, None, None]:
    '''A coroutine that iterates 10 times each time asynchronously
    wait 1 second and yields a random number between 0 and 10.
    '''
    for item in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
