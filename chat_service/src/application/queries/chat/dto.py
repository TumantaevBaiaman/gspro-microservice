from dataclasses import dataclass
from typing import Iterable


@dataclass(slots=True)
class GetChatByIdDTO:
    chat_id: str


@dataclass(slots=True)
class GetChatByUniqueKeyDTO:
    unique_key: str


@dataclass(slots=True)
class ListChatsByIdsDTO:
    chat_ids: Iterable[str]
