import asyncio
import random



async def mock_parse_url(url: str) -> str:
    """
    Mock function for simulating file downloads, has a pre-set chance to fail, and the wait time ranges from 1 to 5 seconds.
    :param url: The url to be downloaded
    :return:
    """

    await asyncio.sleep(random.randint(1,5))
    if random.random() > 0.8:
        raise Exception("Failure downloading file.")

    return "file contents"