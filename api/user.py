from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from cruds import users
from database import get_db
from schemas.user import User, UserCreate, UserUpdate

 
router = APIRouter()


@router.get('/users/{user_id}', response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_todo = users.get_user(db, user_id=user_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return db_todo


@router.get('/users', response_model=List[User])
def read_users(limit: int = 100, db: Session = Depends(get_db)):
    todos = users.get_users(db, limit=limit)
    return todos


@router.post('/users', response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return users.create_user(db=db, user=user)


@router.put('/users/{user_id}', response_model=User)
def update_todo(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return users.update_user(db=db, user_id=user_id, user=user)


@router.delete('/users/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    users.delete_user(db=db, user_id=user_id)
