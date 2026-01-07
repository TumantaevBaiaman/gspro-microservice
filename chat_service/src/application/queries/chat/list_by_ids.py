from src.application.queries.chat.dto import ListChatsByIdsDTO
from src.domain.repositories import IChatRepository


class ListChatsByIdsQuery:

    def __init__(self, repo: IChatRepository):
        self.repo = repo

    async def execute(self, dto: ListChatsByIdsDTO):
        return await self.repo.list_by_ids(dto.chat_ids)
