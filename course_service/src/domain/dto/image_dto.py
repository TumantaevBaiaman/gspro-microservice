from pydantic import BaseModel
from typing import Optional


class UploadImageDTO(BaseModel):
    type: str

    original_url: str
    thumb_small_url: Optional[str] = None
    thumb_medium_url: Optional[str] = None
