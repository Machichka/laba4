from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.all_models import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

async def get_user(db: AsyncSession, user_id: int):
    res = await db.execute(select(User).where(User.id == user_id))
    return res.scalars().first()

async def get_user_by_email(db: AsyncSession, email: str):
    res = await db.execute(select(User).where(User.email == email))
    return res.scalars().first()

async def create_user(db: AsyncSession, user: UserCreate):
    # Зберігаємо пароль лише в соленому вигляді!
    hashed_pwd = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_pwd, is_active=True)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
