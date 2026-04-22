'''
Assignment

Here is your opportunity to keep learning!
1. Create a new route called Users.
2. Then create 2 new API Endpoints
    * get_user: this endpoint should return all information about the user that is currently logged in.
    * change_password: this endpoint should allow a user to change their current password.
'''


from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status

from fastapi import APIRouter, Depends, HTTPException, Path
from models import Todos, Users
from database import SessionLocal
from .auth import get_current_user
from passlib.context import CryptContext


router = APIRouter(
    prefix='/user',tags=['user']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str = Field(min_length=6)


@router.get('/user-details', status_code=status.HTTP_200_OK)
async def get_user(user:user_dependency, db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(Users).filter(Users.id == user.get('id')).first()


@router.put('/change-password', status_code=status.HTTP_204_NO_CONTENT)
async def change_password(request: ChangePasswordRequest, user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    if not bcrypt_context.verify(request.current_password, user_model.hashed_password):
        raise HTTPException(status_code=400, detail='Incorrect current password')
    user_model.hashed_password = bcrypt_context.hash(request.new_password)
    db.add(user_model)
    db.commit()


