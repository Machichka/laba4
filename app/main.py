from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.product import router as product_router
from app.api.category import router as category_router
from app.api.user import router as user_router
from app.api.order import router as order_router

app = FastAPI(
    title="Lab 5 API",
    description="FastAPI з JWT-аутентифікацією в Cookie та bcrypt",
    version="2.0.0"
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(order_router)

@app.get("/")
def root():
    return {"status": "working", "message": "Welcome to Lab 5 API"}