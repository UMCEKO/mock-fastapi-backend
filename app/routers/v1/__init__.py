from fastapi import APIRouter

from . import upload

router = APIRouter(prefix="/v1")

router.include_router(upload.router)