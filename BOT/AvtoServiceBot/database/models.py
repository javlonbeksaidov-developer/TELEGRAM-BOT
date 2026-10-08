from enum import Enum

from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy import Enum as SQL_Enum

from database.db import Base


class UserRoles(Enum):
    ADMIN = "admin"
    USER = "user"


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, nullable=False, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    username = Column(String(255))
    role = Column(SQL_Enum(UserRoles), default=UserRoles.USER)
