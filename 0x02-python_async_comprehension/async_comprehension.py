#!/usr/bin/env python3
"""
This module provides a coroutine that collects 10 random numbers
from an asynchronous generator using async comprehension.
"""


import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using async comprehension.

    Returns:
        List[float]: A list of 10 random floats.
    """
    return [num async for num in async_generator()]
