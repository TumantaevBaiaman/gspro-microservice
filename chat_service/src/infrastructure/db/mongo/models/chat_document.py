from beanie import before_event, Insert, Replace
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

from src.domain.enums.chat_participant_role_enum import ChatParticipantRole
from src.domain.enums.chat_scope_enum import ChatScopeEnum
from .base import BaseDocument


class ChatParticipant(BaseModel):
    user_id: str
    role: ChatParticipantRole
    joined_at: datetime = Field(default_factory=datetime.utcnow)


class ChatDocument(BaseDocument):
    scope: ChatScopeEnum

    course_id: Optional[str] = None

    participants: List[ChatParticipant] = Field(default_factory=list)
    participant_ids: List[str] = Field(default_factory=list)

    last_message_at: Optional[datetime] = None
    is_archived: bool = False

    @before_event(Insert)
    def before_insert(self):
        self._validate()
        self._sync_participant_ids()
        now = datetime.utcnow()
        self.created_at = now
        self.updated_at = now

    @before_event(Replace)
    def before_replace(self):
        self._validate()
        self._sync_participant_ids()
        self.updated_at = datetime.utcnow()

    def _sync_participant_ids(self):
        self.participant_ids = sorted(
            p.user_id for p in self.participants
        )

    def _validate(self):
        if self.scope in (
            ChatScopeEnum.COURSE_GROUP,
            ChatScopeEnum.COURSE_PRIVATE,
        ):
            if not self.course_id:
                raise ValueError(
                    "course_id is required for course chats"
                )

        if self.scope == ChatScopeEnum.DIRECT and self.course_id:
            raise ValueError(
                "direct chat must not have course_id"
            )

        if self.scope == ChatScopeEnum.COURSE_PRIVATE:
            roles = {p.role for p in self.participants}
            if roles != {
                ChatParticipantRole.STUDENT,
                ChatParticipantRole.MENTOR,
            }:
                raise ValueError(
                    "course_private chat must contain student and mentor"
                )

    class Settings:
        name = "chats"
