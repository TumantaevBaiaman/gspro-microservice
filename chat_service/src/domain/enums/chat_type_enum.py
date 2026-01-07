from enum import Enum


class ChatTypeEnum(str, Enum):
    DIRECT = "direct"
    COURSE_GROUP = "course_group"
    COURSE_PRIVATE = "course_private"
