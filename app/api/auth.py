from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.security import verify_password, create_access_token
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.crud import user as crud_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await crud_user.get_user_by_email(db, email=user_in.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await crud_user.create_user(db=db, user=user_in)


@router.post("/login")
async def login(response: Response, user_in: UserLogin, db: AsyncSession = Depends(get_db)):
    user = await crud_user.get_user_by_email(db, email=user_in.email)
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token = create_access_token(data={"sub": user.email})

    # Відправляємо JWT токен у Cookie
    response.set_cookie(
        key="fastapi_token",
        value=access_token,
        httponly=True,
        max_age=3600,
        samesite="lax"
    )
    return {"message": "Successfully logged in"}


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="fastapi_token")
    return {"message": "Successfully logged out"}

