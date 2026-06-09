from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.all_models import Category
from app.schemas.category import CategoryCreate

async def get_category(db: AsyncSession, category_id: int):
    res = await db.execute(select(Category).where(Category.id == category_id))
    return res.scalars().first()

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100):
    res = await db.execute(select(Category).offset(skip).limit(limit))
    return res.scalars().all()

async def create_category(db: AsyncSession, category: CategoryCreate):
    db_cat = Category(**category.model_dump())
    db.add(db_cat)
    await db.commit()
    await db.refresh(db_cat)
    return db_cat
