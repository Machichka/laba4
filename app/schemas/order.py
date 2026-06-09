from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List

class OrderBase(BaseModel):
    user_id: int
    total_amount: float = 0.0

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
