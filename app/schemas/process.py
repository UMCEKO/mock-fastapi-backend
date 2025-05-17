from pydantic import BaseModel
from typing_extensions import Optional


class ProcessRequest(BaseModel):
    urls: list[str]


class Slide(BaseModel):
    slide: int
    summary: Optional[str]
    error: Optional[str]

class Meta(BaseModel):
    total_files: int
    slides_processed: int
    successes: int
    failures: int
    time_elapsed: str


class ProcessResponse(BaseModel):
    results: dict[str, list[Slide]]
    meta: Meta
