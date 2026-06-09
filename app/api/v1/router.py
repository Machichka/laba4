from fastapi import APIRouter
from app.api.v1.endpoints import users, shop

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(shop.router, prefix="/shop", tags=["Shop"])
