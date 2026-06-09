from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.all_models import UserProfile
from app.schemas.user_profile import UserProfileCreate

async def create_profile(db: AsyncSession, profile: UserProfileCreate):
    db_profile = UserProfile(**profile.model_dump())
    db.add(db_profile)
    await db.commit()
    await db.refresh(db_profile)
    return db_profile

async def get_profile_by_user(db: AsyncSession, user_id: int):
    res = await db.execute(select(UserProfile).where(UserProfile.user_id == user_id))
    return res.scalars().first()
