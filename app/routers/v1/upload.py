import uuid
from urllib.parse import urlparse, urlunparse

import magic
from fastapi import APIRouter, UploadFile, HTTPException, File
from typing_extensions import Optional

from app.core.config import S3_BUCKET, MEDIA_URL
from app.schemas.base_response import BaseResponse
from app.schemas.upload import UploadResponse
from app.services.s3_client import s3_client

router = APIRouter(prefix="/upload", tags=["Upload"])

MAX_FILE_SIZE = 10 * 1024 * 1024

@router.post(
    "/",
    response_model=BaseResponse[Optional[UploadResponse]],
    response_description="The pre-signed url of the uploaded file that will last 1 hour.",
    summary = "Upload a PDF file",
    description = (
        "This endpoint allows you to upload PDF documents to be processed later. "
        "The uploaded file is stored and returned as a pre-signed URL valid for 1 hour."
    )
)
async def upload_pdf(file: UploadFile = File(description="The file to be uploaded that will be sent as form data.")):
    # File size and type validation.
    contents = await file.read(size=MAX_FILE_SIZE + 1)
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=422, detail="Failure to upload the image. The file exceeded the 10MB file size limit.")

    mime_type = magic.from_buffer(contents)
    if not mime_type.startswith("PDF document"):
        raise HTTPException(status_code=422, detail="The uploaded document is not a pdf file.")

    # The file url to be uploaded/accessed
    key = f"uploads/{uuid.uuid4().hex}"

    # Upload the file
    s3_client.put_object(
        Bucket=S3_BUCKET,
        Key=key,
        Body=contents,
        ContentType=file.content_type
    )

    # Generate a pre-signed url for security purposes.
    url = s3_client.generate_presigned_url("get_object", Params={
        "Bucket": S3_BUCKET,
        "Key": key,
    })


    # Safely parse and unparse the url in order to avoid injection attacks.
    parsed = urlparse(url)
    custom_url = urlunparse((
        MEDIA_URL.scheme,
        MEDIA_URL.netloc,
        parsed.path,
        parsed.params,
        parsed.query,
        parsed.fragment
    ))

    return BaseResponse(success=True, data=UploadResponse(url=str(custom_url)), message=f"Successful upload.")
