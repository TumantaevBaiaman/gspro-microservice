from src.application.queries.chat.dto import ListUserChatsDTO
from src.domain.repositories import (
    IChatRepository,
    IChatParticipantRepository,
)
from src.infrastructure.db.mongo.models import ChatDocument


class ListUserChatsQuery:

    def __init__(
        self,
        chat_repo: IChatRepository,
        chat_participant_repo: IChatParticipantRepository,
    ):
        self.chat_repo = chat_repo
        self.chat_participant_repo = chat_participant_repo

    async def execute(
        self,
        dto: ListUserChatsDTO,
    ) -> tuple[list[ChatDocument], int]:

        participants, total = await self.chat_participant_repo.list_by_user(
            user_id=dto.user_id,
            limit=dto.limit,
            offset=dto.offset,
        )

        if not participants:
            return [], total

        chat_ids = [p.chat_id for p in participants]

        chats = await self.chat_repo.list_by_ids(
            chat_ids=chat_ids,
            chat_type=dto.chat_type,
        )

        return chats, total
