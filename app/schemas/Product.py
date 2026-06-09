from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    title: str
    description: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    title: Optional[str] = None

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    # Новий синтаксис Pydantic v2 замінь замість orm_mode = True
    model_config = ConfigDict(from_attributes=True)
