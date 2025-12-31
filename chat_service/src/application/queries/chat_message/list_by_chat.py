from src.domain.repositories.chat_message_repository import (
    IChatMessageRepository,
)


class ListChatMessagesQuery:
    def __init__(self, repo: IChatMessageRepository):
        self.repo = repo

    async def execute(
        self,
        *,
        chat_id: str,
        limit: int,
        offset: int,
    ):
        return await self.repo.list_messages(
            chat_id=chat_id,
            limit=limit,
            offset=offset,
        )