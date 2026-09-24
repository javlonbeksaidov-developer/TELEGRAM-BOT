from sqlalchemy import Column, Integer, String, Text

from app.db.db import Base


class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer, nullable=False, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    file_id = Column(String(512), nullable=False)
    duration = Column(Integer, nullable=True)
    file_size = Column(Integer, nullable=True)
    views_count = Column(Integer, default=0)
