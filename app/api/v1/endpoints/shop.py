from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.db.session import get_db
from app.schemas import schemas
from app.crud import crud_shop

router = APIRouter()

@router.post("/categories", response_model=schemas.CategoryResponse, status_code=status.HTTP_201_CREATED)
async def add_category(cat_in: schemas.CategoryCreate, db: AsyncSession = Depends(get_db)):
    return await crud_shop.create_category(db=db, cat_in=cat_in)

@router.get("/categories", response_model=List[schemas.CategoryResponse])
async def list_categories(db: AsyncSession = Depends(get_db)):
    return await crud_shop.get_categories(db=db)

@router.post("/products", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
async def add_product(prod_in: schemas.ProductCreate, db: AsyncSession = Depends(get_db)):
    return await crud_shop.create_product(db=db, prod_in=prod_in)

@router.get("/products", response_model=List[schemas.ProductResponse])
async def list_products(db: AsyncSession = Depends(get_db)):
    return await crud_shop.get_products(db=db)
