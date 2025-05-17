from fastapi import FastAPI, HTTPException
from app.core.config import PORT, HOST
from . import api
from .core.exception_handler import custom_http_exception_handler

app = FastAPI()

app.add_exception_handler(HTTPException, handler=custom_http_exception_handler)

app.include_router(api.router)
