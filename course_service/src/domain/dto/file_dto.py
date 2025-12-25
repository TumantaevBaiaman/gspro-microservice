from pydantic import BaseModel


class UploadFileDTO(BaseModel):
    type: str
    scope: str

    path: str
    filename: str
    mime_type: str
    size_bytes: int
