#!/usr/bin/env python3
"""This module contains functions for asyncio tasks."""


import asyncio
from typing import List
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task that runs wait_random(max_delay).

    Args:
        max_delay (int): The maximum delay time for wait_random.

    Returns:
        asyncio.Task: An asyncio Task object representing the execution
        of wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create asyncio Tasks that call wait_random(max_delay) n times concurrently.

    Args:
        n (int): Number of tasks to create.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
        List[float]: List of delays returned by wait_random in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
