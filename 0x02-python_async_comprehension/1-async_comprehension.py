#!/usr/bin/env python3
"""
Async Comprehension Module
This module contains a coroutine that collects 10 random numbers using
asynchronous comprehension.
"""

from asyncio import run, sleep
from typing import List
from random import uniform
from typing import List

try:
    async_generator = __import__('0-async_generator').async_generator
except ImportError:
    async_generator = None


async def async_comprehension() -> List[float]:
    """
    An asynchronous comprehension that collects 10 random numbers from
    async_generator.
    """
    if async_generator:
        return [i async for i in async_generator()]
    else:
        raise ImportError(
                "Could not import async_generator from 0-async_generator")
