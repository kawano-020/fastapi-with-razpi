from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), index=True)
