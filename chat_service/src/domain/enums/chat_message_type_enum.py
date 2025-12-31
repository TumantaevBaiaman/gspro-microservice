from enum import Enum


class ChatMessageTypeEnum(str, Enum):
    TEXT = "text"
    IMAGE = "image"
    VOICE = "voice"
    FILE = "file"
