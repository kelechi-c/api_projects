from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print(f'Database URL is {SQLALCHEMY_DATABASE_URL}')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

