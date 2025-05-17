import uvicorn
from fastapi import FastAPI, HTTPException
from app.core.config import PORT, HOST
from . import routers
from .core.exception_handler import custom_http_exception_handler

app = FastAPI()

app.add_exception_handler(HTTPException, handler=custom_http_exception_handler)

app.include_router(routers.router)

if __name__ == '__main__':
    uvicorn.run(app, port=PORT, host=HOST)