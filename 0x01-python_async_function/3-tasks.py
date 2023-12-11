#!/usr/bin/env python3
"""
Module that contains a function task_wait_random
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for wait_random(max_delay).

    Args:
        max_delay (int): Maximum delay value.

    Returns:
        asyncio.Task: Task for wait_random(max_delay).
    """
    return asyncio.ensure_future(wait_random(max_delay))
