#!/usr/bin/env python3
"""
This module contains the implementation of a function to measure
the runtime of wait_n.
"""


import asyncio
import time
from typing import List
from concurrent_coroutines import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return
    the average time per call.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        float: The average time per call.
    """
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
