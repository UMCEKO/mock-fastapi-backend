from pydantic import BaseModel
from typing_extensions import Optional, TypeVar, Generic

T = TypeVar('T')

class BaseResponse(BaseModel, Generic[T]):
    message: str
    data: Optional[T] = None
    success: bool
