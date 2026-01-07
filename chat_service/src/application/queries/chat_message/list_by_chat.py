from src.application.queries.chat_message.dto import ListMessagesByChatDTO
from src.domain.repositories import IChatMessageRepository


class ListMessagesByChatQuery:

    def __init__(self, repo: IChatMessageRepository):
        self.repo = repo

    async def execute(self, dto: ListMessagesByChatDTO):
        return await self.repo.list_by_chat(
            chat_id=dto.chat_id,
            limit=dto.limit,
            offset=dto.offset,
        )
