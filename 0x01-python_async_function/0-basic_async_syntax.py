#!/usr/bin/env python3
#asyncio

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Waits for a randdom number of seconds"""
    wait_t = random.random() * max_delay
    await asyncio.sleep(wait_t)
    return wait_t
