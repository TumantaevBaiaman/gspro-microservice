from typing import Optional

from .base_entity import BaseEntity


class CategoryEntity(BaseEntity):
    title: str
    codename: str
    parent_id: Optional[str] = None

    class Settings:
        name = "categories"
        indexes = [
            {
                "fields": [("codename", 1), ("parent_id", 1)],
                "unique": True,
            }
        ]
