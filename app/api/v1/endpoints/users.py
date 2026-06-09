from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.db.session import get_db
from app.schemas import schemas
from app.crud import crud_shop

router = APIRouter()

@router.post("/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
async def create_new_user(user_in: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await crud_shop.get_user_by_email(db, email=user_in.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await crud_shop.create_user(db=db, user_in=user_in)

@router.get("/", response_model=List[schemas.UserResponse])
async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud_shop.get_users(db=db, skip=skip, limit=limit)

@router.put("/{user_id}", response_model=schemas.UserResponse)
async def update_user_profile(user_id: int, user_in: schemas.UserUpdate, db: AsyncSession = Depends(get_db)):
    updated = await crud_shop.update_user(db=db, user_id=user_id, user_in=user_in)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}")
async def delete_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    success = await crud_shop.delete_user(db=db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User successfully deleted"}
