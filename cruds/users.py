from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

from models.user import User
from schemas.user import UserCreate, UserUpdate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, limit: int = 100):
    return db.query(User).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.name = user.name
    db.commit()
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user).first()
    db.delete(db_user)
    db.commit()
