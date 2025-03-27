from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import User
from app.schema import UserRequest, UserResponse

userR = APIRouter()

@userR.get("/users/")
async def read_users(db:Session = Depends(get_db)):
    users = db.query(User).all()
    return list(map(lambda user: UserResponse(**user.__dict__), users))

@userR.post("/users/")
async def create_user(user: UserRequest, db:Session = Depends(get_db)):
    user = db.add(User(**user.model_dump()))
    db.commit()
