from src.application.queries.chat.dto import GetChatByIdDTO
from src.domain.repositories import IChatRepository


class GetChatByIdQuery:

    def __init__(self, repo: IChatRepository):
        self.repo = repo

    async def execute(self, dto: GetChatByIdDTO):
        return await self.repo.get_by_id(dto.chat_id)
