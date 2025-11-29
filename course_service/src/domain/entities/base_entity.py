from beanie import Document
from datetime import datetime


class BaseEntity(Document):
    updated_at: datetime = datetime.utcnow()
    created_at: datetime = datetime.utcnow()
    is_active: bool = True

    class Settings:
        use_state_management = True
        name = None
