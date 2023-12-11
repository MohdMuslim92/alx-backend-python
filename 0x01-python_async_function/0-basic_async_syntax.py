#!/usr/bin/env python3
"""
Module that contains an asynchronous coroutine wait_random
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds (inclusive) and
    returns it.

    Args:
        max_delay (int): Maximum delay value (default 10).

    Returns:
        float: Random delay between 0 and max_delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
