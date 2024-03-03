from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import declarative_base

@declarative_base()
class Base:
    id: Any
    __name__: str
    
    @declared_attr # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
# from typing import Any
# from sqlalchemy.ext.declarative import declared_attr, declarative_base
# # from sqlalchemy.orm import declarative_base

# Base = declarative_base()
# class User(Base):
#     id: Any
#     __name__: str
    
#     @declared_attr # type: ignore
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()