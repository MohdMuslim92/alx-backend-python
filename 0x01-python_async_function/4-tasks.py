#!/usr/bin/env python3
"""
Module that contains functions for asynchronous tasks
"""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Spawns `n` tasks of `task_wait_random` with the specified `max_delay`.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay value.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
