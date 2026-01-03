from src.application.commands.chat_message.send import (
    SendMessageCommand,
)
from src.application.queries.chat_message.list_by_chat import (
    ListChatMessagesQuery,
)
from src.domain.repositories.chat_message_repository import (
    IChatMessageRepository,
)


class ChatMessageService:
    def __init__(self, repo: IChatMessageRepository):
        self.send = SendMessageCommand(repo)
        self.list_by_chat = ListChatMessagesQuery(repo)
