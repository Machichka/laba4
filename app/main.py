from fastapi import FastAPI
from app.api.product import router as product_router
from app.api.category import router as category_router
from app.api.user import router as user_router
from app.api.user_profile import router as profile_router
from app.api.order import router as order_router

app = FastAPI(
    title="Lab 4 API",
    description="Повний backend на FastAPI з підтримкою 5 моделей",
    version="1.0.0"
)

# Підключаємо всі роутери
app.include_router(user_router)
app.include_router(profile_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(order_router)

@app.get("/")
def root():
    return {"status": "working", "message": "Welcome to Lab 4 API"}
