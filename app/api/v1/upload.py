import urllib
import uuid

from urllib.parse import urlparse, urlunparse
from fastapi import APIRouter, UploadFile
from app.core.config import S3_BUCKET, MEDIA_URL
from app.schemas.base_response import BaseResponse
from app.schemas.upload import UploadResponse
from app.services.s3_client import s3_client

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("", response_model=BaseResponse[UploadResponse])
async def upload_file(file: UploadFile):
    # Add file size checks, file type checks.
    print(file.content_type)

    # The file url to be uploaded/accessed
    key = f"uploads/{uuid.uuid4().hex}"

    contents = await file.read()
    # Upload the file
    s3_client.put_object(
        Bucket=S3_BUCKET,
        Key=key,
        Body=contents,
        ContentType=file.content_type
    )

    url = s3_client.generate_presigned_url("get_object", Params={
        "Bucket": S3_BUCKET,
        "Key": key,
    })

    parsed = urlparse(url)
    custom_url = urlunparse((
        MEDIA_URL.scheme,
        MEDIA_URL.netloc,
        parsed.path,
        parsed.params,
        parsed.query,
        parsed.fragment
    ))

    return BaseResponse(success=True, data=UploadResponse(url=str(custom_url)), message="Successful upload.")
