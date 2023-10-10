#!/usr/bin/env python3
"""This module defines the function `measure_time`"""
import asyncio
import random
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for `wait_n(n, max_delay)`"""
    startTime = time.time()

    asyncio.run(wait_n(n, max_delay))

    endTime = time.time()

    return (endTime - startTime) / n
