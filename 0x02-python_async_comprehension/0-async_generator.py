#!/usr/bin/env python3
"""
Async Generator Module
This module contains an asynchronous generator that yields random numbers after
waiting 1 second asynchronously.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator that yields random numbers after waiting 1 second
    asynchronously.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
