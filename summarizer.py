import random
import asyncio

async def summarize_slide(text: str) -> str:
    # Simulate random API failure
    await asyncio.sleep(0.5)
    if random.random() < 0.3:
        raise TimeoutError("LLM timed out.")
    return f"Summary of: {text}"
