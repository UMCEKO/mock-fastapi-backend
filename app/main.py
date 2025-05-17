import uvicorn
from fastapi import FastAPI, HTTPException

from app.core.config import PORT, HOST, S3_BUCKET
from app.services.s3_client import s3_client, setup_s3
from . import routers
from .core.exception_handler import custom_http_exception_handler

app = FastAPI()

app.add_exception_handler(HTTPException, handler=custom_http_exception_handler)

app.include_router(routers.router)


# Check if the bucket exists and create if it does not

def main():
    setup_s3()
    uvicorn.run(app, port=PORT, host=HOST)