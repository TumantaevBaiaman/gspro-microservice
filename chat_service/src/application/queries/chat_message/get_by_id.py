from src.application.queries.chat_message.dto import GetMessageByIdDTO
from src.domain.repositories import IChatMessageRepository


class GetMessageByIdQuery:

    def __init__(self, repo: IChatMessageRepository):
        self.repo = repo

    async def execute(self, dto: GetMessageByIdDTO):
        return await self.repo.get_by_id(dto.message_id)
