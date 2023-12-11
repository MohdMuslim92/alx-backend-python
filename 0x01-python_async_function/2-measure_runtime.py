#!/usr/bin/env python3
"""
Module that contains a measure_time function
"""

import asyncio
import time
from typing import Callable


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    total_time / n.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay value.

    Returns:
        float: Average time taken for each task.
    """
    start_time = time.time()

    # Importing wait_n here to avoid circular imports
    wait_n = __import__('1-concurrent_coroutines').wait_n

    asyncio.run(wait_n(n, max_delay))

    total_time = time.time() - start_time
    return total_time / n
