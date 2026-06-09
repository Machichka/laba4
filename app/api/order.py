from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.schemas.order import OrderCreate, OrderResponse
from app.crud import order as crud_order
from app.api.deps import get_current_user
from app.models.all_models import User

router = APIRouter(prefix="/orders", tags=["Orders"])

# ЗАХИЩЕНА РУЧКА 2: Створення замовлення (user_id береться примусово з токена)
@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_new_order(order: OrderCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    order.user_id = current_user.id
    return await crud_order.create_order(db=db, order=order)

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_new_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    return await crud_order.create_order(db=db, order=order)

@router.get("/user/{user_id}", response_model=List[OrderResponse])
async def read_user_orders(user_id: int, db: AsyncSession = Depends(get_db)):
    return await crud_order.get_user_orders(db=db, user_id=user_id)
