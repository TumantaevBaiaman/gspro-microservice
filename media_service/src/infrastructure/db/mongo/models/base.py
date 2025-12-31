from beanie import Document, before_event, Insert, Replace
from datetime import datetime
from pydantic import Field


class BaseDocument(Document):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True

    @before_event(Insert)
    def set_created(self):
        now = datetime.utcnow()
        self.created_at = now
        self.updated_at = now

    @before_event(Replace)
    def set_updated(self):
        self.updated_at = datetime.utcnow()

    class Settings:
        use_state_management = True
        name = None
