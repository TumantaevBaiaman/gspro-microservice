from src.application.queries.chat.dto import GetChatByUniqueKeyDTO
from src.domain.repositories import IChatRepository


class GetChatByUniqueKeyQuery:

    def __init__(self, repo: IChatRepository):
        self.repo = repo

    async def execute(self, dto: GetChatByUniqueKeyDTO):
        return await self.repo.get_by_unique_key(dto.unique_key)
