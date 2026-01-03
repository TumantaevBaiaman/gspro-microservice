from enum import Enum


class ChatScopeEnum(str, Enum):
    COURSE_GROUP = "course_group"
    COURSE_PRIVATE = "course_private"
    DIRECT = "direct"
