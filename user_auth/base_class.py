from typing import Any
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import Mapped, as_declarative

# Base = declarative_base()

# class User(Base):
#     id: Mapped[int] = Column(Integer, primary_key=True)

#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()

@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()