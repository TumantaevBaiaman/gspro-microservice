from datetime import datetime
from typing import List, Optional, Tuple

from pymongo.errors import DuplicateKeyError

from src.domain.enums.chat_scope_enum import ChatScopeEnum
from src.infrastructure.db.mongo.models.chat_document import (
    ChatDocument,
    ChatParticipant,
)
from src.infrastructure.db.mongo.models.chat_message_document import (
    ChatMessageDocument,
    ChatMessagePayload,
    ChatMessageContext,
)
from src.domain.repositories import IChatMessageRepository


class ChatMessageRepository(IChatMessageRepository):
    async def send_message(
        self,
        *,
        scope: ChatScopeEnum,
        sender_id: str,
        participants: List[ChatParticipant],
        payload: ChatMessagePayload,
        course_id: Optional[str] = None,
        context: Optional[ChatMessageContext] = None,
    ) -> Tuple[ChatDocument, ChatMessageDocument]:

        participant_ids = self._normalize_participants(participants)

        chat = await self._find_or_create_chat(
            scope=scope,
            course_id=course_id,
            participants=participants,
            participant_ids=participant_ids,
        )

        message = await self._create_message(
            chat_id=str(chat.id),
            sender_id=sender_id,
            payload=payload,
            context=context,
        )

        await self._touch_chat(chat)

        return chat, message

    async def list_messages(
        self,
        *,
        chat_id: str,
        limit: int,
        offset: int,
    ) -> Tuple[List[ChatMessageDocument], int]:
        query = ChatMessageDocument.find(
            ChatMessageDocument.chat_id == chat_id
        )

        total = await query.count()

        items = await (
            query
            .sort("meta.created_at")
            .skip(offset)
            .limit(limit)
            .to_list()
        )

        return items, total

    async def _find_or_create_chat(
        self,
        *,
        scope: ChatScopeEnum,
        course_id: Optional[str],
        participants: List[ChatParticipant],
        participant_ids: List[str],
    ) -> ChatDocument:

        chat = await self._find_chat(
            scope=scope,
            course_id=course_id,
            participant_ids=participant_ids,
        )

        if chat:
            return chat

        try:
            chat = ChatDocument(
                scope=scope,
                course_id=course_id,
                participants=participants,
            )
            await chat.insert()
            return chat

        except DuplicateKeyError:
            chat = await self._find_chat(
                scope=scope,
                course_id=course_id,
                participant_ids=participant_ids,
            )
            if not chat:
                raise RuntimeError("Chat creation race condition")
            return chat

    async def _find_chat(
        self,
        *,
        scope: ChatScopeEnum,
        course_id: Optional[str],
        participant_ids: List[str],
    ) -> Optional[ChatDocument]:

        if scope == ChatScopeEnum.COURSE_GROUP:
            return await ChatDocument.find_one(
                ChatDocument.scope == scope,
                ChatDocument.course_id == course_id,
            )

        if scope == ChatScopeEnum.COURSE_PRIVATE:
            return await ChatDocument.find_one(
                ChatDocument.scope == scope,
                ChatDocument.course_id == course_id,
                ChatDocument.participant_ids == participant_ids,
            )

        if scope == ChatScopeEnum.DIRECT:
            return await ChatDocument.find_one(
                ChatDocument.scope == scope,
                ChatDocument.participant_ids == participant_ids,
            )

        raise ValueError(f"Unsupported chat scope: {scope}")

    async def _create_message(
        self,
        *,
        chat_id: str,
        sender_id: str,
        payload: ChatMessagePayload,
        context: Optional[ChatMessageContext],
    ) -> ChatMessageDocument:

        message = ChatMessageDocument(
            chat_id=chat_id,
            sender_id=sender_id,
            payload=payload,
            context=context or ChatMessageContext(),
        )

        await message.insert()
        return message

    async def _touch_chat(self, chat: ChatDocument) -> None:
        chat.last_message_at = datetime.utcnow()
        await chat.replace()

    @staticmethod
    def _normalize_participants(
        participants: List[ChatParticipant],
    ) -> List[str]:
        return sorted(p.user_id for p in participants)
