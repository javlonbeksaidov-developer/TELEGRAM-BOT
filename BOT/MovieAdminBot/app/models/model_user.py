from sqlalchemy import BigInteger, Column, Integer, String

from app.db.db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    user_id = Column(Integer, nullable=False, index=True)
    username = Column(String(255))
