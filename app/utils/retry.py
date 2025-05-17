from functools import wraps


def retry_async(retry_count: int = 3):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            remaining_tries = retry_count
            last_exception = None
            while remaining_tries > 0:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    remaining_tries -= 1
                    last_exception = e
            raise last_exception
        return wrapper
    return decorator
