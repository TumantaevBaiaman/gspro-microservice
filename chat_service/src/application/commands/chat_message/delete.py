from src.application.commands.chat_message.dto import DeleteMessageDTO
from src.domain.repositories import IChatMessageRepository


class DeleteMessageCommand:

    def __init__(self, message_repo: IChatMessageRepository):
        self.message_repo = message_repo

    async def execute(self, dto: DeleteMessageDTO):
        message = await self.message_repo.get_by_id(dto.message_id)
        if not message:
            return None

        if message.sender_id != dto.user_id:
            raise PermissionError("Cannot delete чужое сообщение")

        await self.message_repo.soft_delete(
            message_id=dto.message_id,
        )
        return message
