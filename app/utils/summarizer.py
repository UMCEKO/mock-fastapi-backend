import asyncio
import random

from app.utils.retry import retry_async


@retry_async(retry_count=3)
async def summarize_with_claude(block) -> str:
    await asyncio.sleep(random.randint(1,5))
    if random.random() < 0.2:
        raise Exception("Failure downloading file.")

    return block[::40]

@retry_async(retry_count=3)
async def summarize_with_gpt(block) -> str:
    await asyncio.sleep(random.randint(1,5))
    if random.random() < 0.2:
        raise Exception("Failure downloading file.")

    return block[::40]

@retry_async(retry_count=3)
async def fallback_summary(block) -> str:
    await asyncio.sleep(random.randint(1,5))
    if random.random() < 0.2:
        raise Exception("Failure downloading file.")

    return block[::40]