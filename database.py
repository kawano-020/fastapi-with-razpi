from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


user_name = 'root'
password = ''
host = '127.0.0.1'
database_name = 'razpi'

DATABASE = f'mysql+mysqlconnector://{user_name}:{password}@{host}/{database_name}?charset=utf8'

ENGINE = create_engine(
    DATABASE,
    encoding='utf-8',
    echo=True
)

session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

Base = declarative_base()
Base.query = session.query_property()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
