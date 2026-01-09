from src.application.commands.chat_participant.dto import UpdateLastReadDTO
from src.domain.repositories import IChatParticipantRepository


class UpdateLastReadCommand:

    def __init__(self, repo: IChatParticipantRepository):
        self.repo = repo

    async def execute(self, dto: UpdateLastReadDTO) -> None:
        await self.repo.update_last_read(
            chat_id=dto.chat_id,
            user_id=dto.user_id,
            last_read_at=dto.last_read_at,
        )
