from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.user_profile import UserProfileCreate, UserProfileResponse
from app.crud import user_profile as crud_profile

router = APIRouter(prefix="/profiles", tags=["User Profiles"])

@router.post("/", response_model=UserProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_user_profile(profile: UserProfileCreate, db: AsyncSession = Depends(get_db)):
    existing = await crud_profile.get_profile_by_user(db, profile.user_id)
    if existing:
        raise HTTPException(status_code=400, detail="Profile already exists for this user")
    return await crud_profile.create_profile(db=db, profile=profile)
