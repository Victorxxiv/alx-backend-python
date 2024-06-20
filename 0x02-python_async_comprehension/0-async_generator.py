#!/usr/bin/env python3
"""
This module write a coroutine called async_generator that takes no arguments.
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields a random float between 0 and 10,
    once per second, for a total of 10 times.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
