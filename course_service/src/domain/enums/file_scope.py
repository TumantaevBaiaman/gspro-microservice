from enum import Enum


class FileScope(str, Enum):
    COURSE = "course"
    MODULE = "module"
    LESSON = "lesson"
