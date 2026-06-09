import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings
from app.models.all_models import Base, User, UserProfile, Category, Product, Order

# Створюємо тимчасовий двигун для скрипта
engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def seed_data():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            print("Початок наповнення бази даних...")

            # 1. Додаємо категорії
            cat1 = Category(name="Електроніка")
            cat2 = Category(name="Автотовари")
            session.add_all([cat1, cat2])
            await session.flush()  # Отримуємо ID категорій

            # 2. Додаємо товари
            prod1 = Product(title="Ноутбук Lenovo", description="Чудовий робочий інструмент", price=25000.0, category_id=cat1.id)
            prod2 = Product(title="Моторна олива 5W-40", description="Синтетична олива для двигуна", price=1200.0, category_id=cat2.id)
            session.add_all([prod1, prod2])

            # 3. Додаємо користувачів
            user1 = User(email="admin@example.com", hashed_password="superpassword123", is_active=True)
            user2 = User(email="user@example.com", hashed_password="userpassword456", is_active=True)
            session.add_all([user1, user2])
            await session.flush()  # Отримуємо ID користувачів

            # 4. Додаємо профілі користувачів (Зв'язок 1:1)
            profile1 = UserProfile(user_id=user1.id, first_name="Олександр", last_name="Адмін", phone="+380991112233")
            profile2 = UserProfile(user_id=user2.id, first_name="Іван", last_name="Тестер", phone="+380674445566")
            session.add_all([profile1, profile2])

            # 5. Додаємо замовлення (Зв'язок 1:M)
            order1 = Order(user_id=user1.id, total_amount=25000.0)
            order2 = Order(user_id=user2.id, total_amount=1200.0)
            session.add_all([order1, order2])

        await session.commit()
        print("Базу даних успішно наповнено тестовими даними!")

if __name__ == "__main__":
    asyncio.run(seed_data())
