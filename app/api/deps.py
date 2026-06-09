from fastapi import Request, HTTPException, Depends, status
import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.core.database import get_db
from app.crud import user as crud_user
from app.models.all_models import User


async def get_current_user(request: Request, db: AsyncSession = Depends(get_db)) -> User:
    # Витягуємо токен з кукі, як вимагає лаба
    token = request.cookies.get("fastapi_token")

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

    user = await crud_user.get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user

