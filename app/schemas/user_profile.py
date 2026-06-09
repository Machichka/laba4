from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserProfileBase(BaseModel):
    user_id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None

class UserProfileCreate(UserProfileBase):
    pass

class UserProfileResponse(UserProfileBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
