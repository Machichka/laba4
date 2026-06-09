from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.schemas.order import OrderCreate, OrderResponse
from app.crud import order as crud_order

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_new_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    return await crud_order.create_order(db=db, order=order)

@router.get("/user/{user_id}", response_model=List[OrderResponse])
async def read_user_orders(user_id: int, db: AsyncSession = Depends(get_db)):
    return await crud_order.get_user_orders(db=db, user_id=user_id)
