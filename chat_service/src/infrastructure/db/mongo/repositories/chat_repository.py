from beanie.odm.operators.find.comparison import In
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
        chat_type: ChatTypeEnum | None = None,
    ) -> list[ChatDocument]:
        if not chat_ids:
            return []

        ids = [PydanticObjectId(cid) for cid in chat_ids]

        filters = [
            In(ChatDocument.id, ids),
            ChatDocument.is_archived == False,
        ]

        if chat_type:
            filters.append(ChatDocument.type == chat_type)

        return await (
            ChatDocument.find(*filters)
            .sort("-last_message_at")
            .to_list()
        )

    async def list_private_by_course(
            self,
            course_id: str,
    ) -> list[ChatDocument]:
        prefix = f"chat:course:private:{course_id}:"

        chats =  await ChatDocument.find(
            {
                "type": ChatTypeEnum.COURSE_PRIVATE,
                "unique_key": {"$regex": f"^{prefix}"},
                "is_archived": False,
            }
        ).sort("-last_message_at").to_list()
        print(chats)
        return chats