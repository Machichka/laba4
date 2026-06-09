from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.all_models import User
from app.schemas.user import UserCreate

async def get_user(db: AsyncSession, user_id: int):
    res = await db.execute(select(User).where(User.id == user_id))
    return res.scalars().first()

async def create_user(db: AsyncSession, user: UserCreate):
    # Тимчасово мапимо password в твій hashed_password для лаби 4
    db_user = User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
