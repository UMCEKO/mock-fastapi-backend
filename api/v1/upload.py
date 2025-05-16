from schemas.BaseResponse import BaseResponse

async def upload_file():
    url: str = ""



    return BaseResponse(success=True, data={
        "url": url
    }, message="Successful upload.")