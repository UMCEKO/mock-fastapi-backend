import asyncio
import random


async def summarize_with_claude(block) -> str:
    await asyncio.sleep(random.randint(1,5))
    if random.random() > 0.8:
        raise Exception("Failure downloading file.")

    return block[::40]

async def summarize_with_gpt(block) -> str:
    await asyncio.sleep(random.randint(1,5))
    if random.random() > 0.8:
        raise Exception("Failure downloading file.")

    return block[::40]

async def fallback_summary(block) -> str:
    await asyncio.sleep(random.randint(1,5))
    if random.random() > 0.8:
        raise Exception("Failure downloading file.")

    return block[::40]