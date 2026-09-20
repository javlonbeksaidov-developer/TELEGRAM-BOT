from db.database import Base
from sqlalchemy import BigInteger, Column, Integer, String


class Users(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=True)
    user_id = Column(BigInteger, unique=True, nullable=False, index=True)
    full_name = Column(String(255), nullable=False)
