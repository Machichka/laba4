from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.models.all_models import User, UserProfile, Category, Product, Order
from app.schemas import schemas

# --- USER & PROFILE CRUD ---
async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email).options(selectinload(User.profile)))
    return result.scalars().first()

async def create_user(db: AsyncSession, user_in: schemas.UserCreate):
    db_user = User(email=user_in.email, hashed_password=user_in.password + "fake_hash") # Спрощено для лаби
    db.add(db_user)
    await db.flush() # щоб отримати id користувача
    
    profile_data = user_in.profile.model_dump() if user_in.profile else {}
    db_profile = UserProfile(user_id=db_user.id, **profile_data)
    db.add(db_profile)
    
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(User).options(selectinload(User.profile)).offset(skip).limit(limit))
    return result.scalars().all()

async def update_user(db: AsyncSession, user_id: int, user_in: schemas.UserUpdate):
    result = await db.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().first()
    if db_user:
        for field, value in user_in.model_dump(exclude_unset=True).items():
            setattr(db_user, field, value)
        await db.commit()
        await db.refresh(db_user)
    return db_user

async def delete_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().first()
    if db_user:
        await db.delete(db_user)
        await db.commit()
        return True
    return False

# --- CATEGORY & PRODUCT CRUD ---
async def create_category(db: AsyncSession, cat_in: schemas.CategoryCreate):
    db_cat = Category(name=cat_in.name)
    db.add(db_cat)
    await db.commit()
    await db.refresh(db_cat)
    return db_cat

async def get_categories(db: AsyncSession):
    result = await db.execute(select(Category))
    return result.scalars().all()

async def create_product(db: AsyncSession, prod_in: schemas.ProductCreate):
    db_prod = Product(**prod_in.model_dump())
    db.add(db_prod)
    await db.commit()
    await db.refresh(db_prod)
    return db_prod

async def get_products(db: AsyncSession):
    result = await db.execute(select(Product))
    return result.scalars().all()
