from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.base_response import BaseResponse

async def custom_http_exception_handler(request: Request, exc: Exception):
    if not isinstance(exc, HTTPException):
        raise exc
    return JSONResponse(
        status_code=exc.status_code,
        content=BaseResponse(
            success=False,
            message=exc.detail,
            data=None
        ).model_dump()
    )