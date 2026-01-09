from src.application.queries.chat_participant.dto import ListChatIdsByUserDTO
from src.domain.repositories import IChatParticipantRepository


class ListChatIdsByUserQuery:

    def __init__(self, repo: IChatParticipantRepository):
        self.repo = repo

    async def execute(self, dto: ListChatIdsByUserDTO) -> list[str]:
        return await self.repo.list_chat_ids_by_user(
            user_id=dto.user_id
        )
