from fastapi import APIRouter, Depends,status
from app.schemas.user import UserCreate
from app.db.db import get_db
from app.models.user import UserModel
from sqlalchemy.orm import Session





router = APIRouter(prefix="/user", tags=["User"])



@router.post("/", status_code=status.HTTP_201_CREATED)
async def registration(user:UserCreate,db: Session = Depends(get_db)):
    new_user = UserModel(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", status_code=status.HTTP_200_OK)
async def read_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users