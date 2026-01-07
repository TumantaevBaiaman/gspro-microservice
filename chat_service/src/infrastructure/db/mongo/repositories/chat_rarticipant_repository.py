from datetime import datetime

from src.domain.enums.chat_participant_role_enum import ChatParticipantRole
from src.domain.repositories.chat_participant_repository import (
    IChatParticipantRepository,
)
from src.infrastructure.db.mongo.models import ChatParticipantDocument


class ChatParticipantRepository(IChatParticipantRepository):

    async def add_participant(
        self,
        *,
        chat_id: str,
        user_id: str,
        role: ChatParticipantRole,
    ) -> None:
        exists = await self.exists(chat_id=chat_id, user_id=user_id)
        if exists:
            return

        await ChatParticipantDocument(
            chat_id=chat_id,
            user_id=user_id,
            role=role,
        ).insert()

    async def exists(
        self,
        *,
        chat_id: str,
        user_id: str,
    ) -> bool:
        doc = await ChatParticipantDocument.find_one(
            ChatParticipantDocument.chat_id == chat_id,
            ChatParticipantDocument.user_id == user_id,
        )
        return doc is not None

    async def list_by_chat(
        self,
        *,
        chat_id: str,
    ) -> list[ChatParticipantDocument]:
        return await ChatParticipantDocument.find(
            ChatParticipantDocument.chat_id == chat_id
        ).to_list()

    async def list_chat_ids_by_user(
        self,
        *,
        user_id: str,
    ) -> list[str]:
        participants = await ChatParticipantDocument.find(
            ChatParticipantDocument.user_id == user_id,
            ChatParticipantDocument.is_archived == False,
        ).to_list()

        return [p.chat_id for p in participants]

    async def update_last_read(
        self,
        *,
        chat_id: str,
        user_id: str,
        last_read_at: datetime,
    ) -> None:
        await ChatParticipantDocument.find_one(
            ChatParticipantDocument.chat_id == chat_id,
            ChatParticipantDocument.user_id == user_id,
        ).update_one(
            {
                "$set": {
                    "last_read_at": last_read_at,
                }
            }
        )

    async def set_muted(
        self,
        *,
        chat_id: str,
        user_id: str,
        value: bool,
    ) -> None:
        await ChatParticipantDocument.find_one(
            ChatParticipantDocument.chat_id == chat_id,
            ChatParticipantDocument.user_id == user_id,
        ).update_one(
            {
                "$set": {
                    "is_muted": value,
                }
            }
        )

    async def set_archived(
        self,
        *,
        chat_id: str,
        user_id: str,
        value: bool,
    ) -> None:
        await ChatParticipantDocument.find_one(
            ChatParticipantDocument.chat_id == chat_id,
            ChatParticipantDocument.user_id == user_id,
        ).update_one(
            {
                "$set": {
                    "is_archived": value,
                }
            }
        )
