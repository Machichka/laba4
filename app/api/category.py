from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.schemas.category import CategoryCreate, CategoryResponse
from app.crud import category as crud_category

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_item(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    return await crud_category.create_category(db=db, category=category)

@router.get("/", response_model=List[CategoryResponse])
async def read_items(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud_category.get_categories(db=db, skip=skip, limit=limit)
