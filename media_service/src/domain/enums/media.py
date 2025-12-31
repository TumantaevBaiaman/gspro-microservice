from enum import Enum


class OwnerService(str, Enum):
    course = "course"
    user = "user"
    chat = "chat"


class MediaKind(str, Enum):
    image = "image"
    audio = "audio"
    video = "video"
    file = "file"


class MediaUsage(str, Enum):
    cover = "cover"
    avatar = "avatar"
    lesson = "lesson"
    message = "message"


class MediaStatus(str, Enum):
    draft = "draft"
    attached = "attached"

