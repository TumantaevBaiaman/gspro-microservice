from datetime import datetime
from beanie import PydanticObjectId

from src.domain.repositories.chat_message_repository import (
    IChatMessageRepository,
)
from src.infrastructure.db.mongo.models import ChatMessageDocument


class ChatMessageRepository(IChatMessageRepository):

    async def create(
        self,
        *,
        chat_id: str,
        sender_id: str,
        payload,
        context,
    ) -> ChatMessageDocument:
        message = ChatMessageDocument(
            chat_id=chat_id,
            sender_id=sender_id,
            payload=payload,
            context=context,
        )
        await message.insert()
        return message

    async def get_by_id(
        self,
        message_id: str,
    ) -> ChatMessageDocument | None:
        return await ChatMessageDocument.get(
            PydanticObjectId(message_id)
        )

    async def list_by_chat(
        self,
        *,
        chat_id: str,
        limit: int = 50,
        offset: int = 0,
    ) -> list[ChatMessageDocument]:
        return await (
            ChatMessageDocument.find(
                ChatMessageDocument.chat_id == chat_id,
                ChatMessageDocument.meta.deleted_at == None,
            )
            .sort("-created_at")
            .skip(offset)
            .limit(limit)
            .to_list()
        )

    async def list_by_reference(
        self,
        *,
        chat_id: str,
        reference_type: str,
        reference_id: str,
        limit: int = 50,
        offset: int = 0,
    ) -> list[ChatMessageDocument]:
        return await (
            ChatMessageDocument.find(
                ChatMessageDocument.chat_id == chat_id,
                ChatMessageDocument.context.reference.type == reference_type,
                ChatMessageDocument.context.reference.id == reference_id,
                ChatMessageDocument.meta.deleted_at == None,
            )
            .sort("-created_at")
            .skip(offset)
            .limit(limit)
            .to_list()
        )

    async def update_text(
        self,
        *,
        message_id: str,
        new_text: str,
    ) -> None:
        await ChatMessageDocument.find_one(
            ChatMessageDocument.id == PydanticObjectId(message_id)
        ).update_one(
            {
                "$set": {
                    "payload.text": new_text,
                    "meta.edited_at": datetime.utcnow(),
                }
            }
        )

    async def soft_delete(
        self,
        *,
        message_id: str,
    ) -> None:
        await ChatMessageDocument.find_one(
            ChatMessageDocument.id == PydanticObjectId(message_id)
        ).update_one(
            {
                "$set": {
                    "meta.deleted_at": datetime.utcnow(),
                }
            }
        )
