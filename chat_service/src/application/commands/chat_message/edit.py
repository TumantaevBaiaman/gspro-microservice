from src.application.commands.chat_message.dto import EditMessageDTO
from src.domain.repositories import IChatMessageRepository


class EditMessageCommand:

    def __init__(self, message_repo: IChatMessageRepository):
        self.message_repo = message_repo

    async def execute(self, dto: EditMessageDTO):
        message = await self.message_repo.get_by_id(dto.message_id)
        if not message:
            return None

        if message.sender_id != dto.editor_id:
            raise PermissionError("Cannot edit чужое сообщение")

        await self.message_repo.update_text(
            message_id=dto.message_id,
            new_text=dto.new_text,
        )
        return message
