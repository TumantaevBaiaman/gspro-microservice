from .base_entity import BaseEntity
from src.domain.enums.file_type import FileType
from src.domain.enums.file_scope import FileScope


class FileEntity(BaseEntity):
    type: FileType

    scope: FileScope

    path: str
    filename: str
    mime_type: str
    size_bytes: int

    class Settings:
        name = "files"
