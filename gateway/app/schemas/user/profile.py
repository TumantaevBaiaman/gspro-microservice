from typing import Optional

from pydantic import BaseModel


class GetUserProfileResponseSchema(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    city: Optional[str] = None
    industry: Optional[str] = None
    experience_level: Optional[str] = None