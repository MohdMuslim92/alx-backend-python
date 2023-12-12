#!/usr/bin/env python3
"""
Measure Runtime Module
This module contains a coroutine that measures the total runtime by executing
async_comprehension four times in parallel using asyncio.gather.
"""

import asyncio
from typing import List
from time import perf_counter

try:
    async_comprehension = __import__(
            '1-async_comprehension').async_comprehension
except ImportError:
    async_comprehension = None


async def measure_runtime() -> float:
    """
    A coroutine that measures the total runtime by executing
    async_comprehension four times in parallel using asyncio.gather.
    """
    start_time = perf_counter()

    if async_comprehension:
        await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
        )

    end_time = perf_counter()
    return end_time - start_time
