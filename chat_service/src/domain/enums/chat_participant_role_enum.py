from enum import Enum


class ChatParticipantRole(str, Enum):
    STUDENT = "student"
    MENTOR = "mentor"
