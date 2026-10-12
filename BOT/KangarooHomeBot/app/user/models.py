from datetime import UTC, datetime

from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from config.db import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=True)

    users = relationship("Users", secondary="user_roles", back_populates="roles")


class UserRoles(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"))


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    # Veb ilova uchun
    username = Column(String(255), nullable=True, unique=True)
    password = Column(String(512), nullable=True)
    email = Column(String(255), nullable=True)

    # Telegram bot uchun
    user_id = Column(BigInteger, nullable=True, unique=True, index=True)
    tg_username = Column(String(255), nullable=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)

    # Qo'shimcha
    year = Column(Integer, nullable=True)
    phone = Column(String(20), nullable=True)

    roles = relationship(
        "Role", secondary="user_roles", back_populates="users", lazy="joined"
    )

    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
