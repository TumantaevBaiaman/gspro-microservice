from src.application.queries.chat_message.dto import ListMessagesByReferenceDTO
from src.domain.repositories import IChatMessageRepository


class ListMessagesByReferenceQuery:

    def __init__(self, repo: IChatMessageRepository):
        self.repo = repo

    async def execute(self, dto: ListMessagesByReferenceDTO):
        return await self.repo.list_by_reference(
            chat_id=dto.chat_id,
            reference_type=dto.reference_type,
            reference_id=dto.reference_id,
            limit=dto.limit,
            offset=dto.offset,
        )
