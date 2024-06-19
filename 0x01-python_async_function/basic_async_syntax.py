#!/usr/bin/env python3
"""This module contains the implementation of an asynchronous coroutine."""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for random delay between 0 and max_delay seconds and return the delay.

    Args:
        max_delay (int): The maximum delay time in seconds. Defaults to 10.

    Returns:
        frloat" The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
