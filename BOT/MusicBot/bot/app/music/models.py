from db.database import Base
from sqlalchemy import BigInteger, Column, Integer, String


class Musics(Base):
    __tablename__ = "musics"

    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(String(255), unique=True, index=True, nullable=False)
    title = Column(String(255), nullable=False)
    performer = Column(String(255), nullable=True)
    file_name = Column(String(255), nullable=True)
    duration = Column(Integer, nullable=True)
    file_size = Column(BigInteger, nullable=True)
