from enum import Enum


class UserRole(str, Enum):
    user = "user"
    admin = "admin"
    moderator = "moderator"
    mentor = "mentor"
