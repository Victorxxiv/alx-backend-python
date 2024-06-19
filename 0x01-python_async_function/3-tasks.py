#!/usr/bin/env python3
"""
This module contains the implementation of a function returning an
asyncio.Task.
"""


import asyncio
from typing import Union
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task that runs wait_random(max_delay).

    Args:
        max_delay (int): The maximum delay time for wait_random.

    Returns:
        asyncio.Task: An asyncio Task object representing the
        execution of wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
