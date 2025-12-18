from dataclasses import dataclass
from uuid import UUID


@dataclass
class UserCategoryEntity:
    id: UUID
    user_id: UUID
    category_id: UUID

