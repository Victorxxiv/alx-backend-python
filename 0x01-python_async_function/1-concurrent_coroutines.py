#!/usr/bin/env python3
"""
This module contains the implementation of an async routine that
spawns multiple tasks.
"""


import asyncio
from typing import List
from 0_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(delays)
