from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# --- Схеми Профілю ---
class ProfileBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None

class ProfileCreate(ProfileBase):
    pass

class ProfileResponse(ProfileBase):
    id: int
    user_id: int
    class Config: from_attributes = True

# --- Схеми Користувача ---
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    profile: Optional[ProfileCreate] = None

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    is_active: bool
    profile: Optional[ProfileResponse] = None
    class Config: from_attributes = True

# --- Схеми Категорій та Товарів ---
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    class Config: from_attributes = True

class ProductBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category_id: Optional[int] = None

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    class Config: from_attributes = True
