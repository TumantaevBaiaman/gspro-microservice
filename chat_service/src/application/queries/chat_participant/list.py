from src.application.queries.chat_participant.dto import ListChatParticipantsDTO
from src.domain.repositories import IChatParticipantRepository


class ListChatParticipantsQuery:

    def __init__(self, repo: IChatParticipantRepository):
        self.repo = repo

    async def execute(self, dto: ListChatParticipantsDTO):
        return await self.repo.list_by_chat(
            chat_id=dto.chat_id
        )
