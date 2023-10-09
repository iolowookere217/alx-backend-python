#!/usr/bin/env python3
"""This module defines an asynchronous function `wait_random`"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that waits for a random delay
        and eventually returns it
    """
    wait: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
