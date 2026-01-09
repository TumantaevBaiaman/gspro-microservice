from pymongo.errors import DuplicateKeyError
from beanie import PydanticObjectId

from src.domain.enums.chat_type_enum import ChatTypeEnum
from src.infrastructure.db.mongo.models import ChatDocument
from src.domain.repositories.chat_repository import IChatRepository


class ChatRepository(IChatRepository):

    async def get_by_id(
        self,
        chat_id: str,
    ) -> ChatDocument | None:
        return await ChatDocument.get(PydanticObjectId(chat_id))

    async def get_by_unique_key(
        self,
        unique_key: str,
    ) -> ChatDocument | None:
        return await ChatDocument.find_one(
            ChatDocument.unique_key == unique_key
        )

    async def create(
        self,
        *,
        type: ChatTypeEnum,
        course_id: str | None,
        unique_key: str,
    ) -> ChatDocument:
        chat = ChatDocument(
            type=type,
            course_id=course_id,
            unique_key=unique_key,
        )

        try:
            await chat.insert()
            return chat
        except DuplicateKeyError:
            existing = await self.get_by_unique_key(unique_key)
            if not existing:
                raise
            return existing

    async def list_by_ids(
        self,
        chat_ids,
    ) -> list[ChatDocument]:
        if not chat_ids:
            return []

        return await ChatDocument.find(
            ChatDocument.id.in_(
                [PydanticObjectId(cid) for cid in chat_ids]
            )
        ).sort("-last_message_at").to_list()
