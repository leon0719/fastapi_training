from database import Base
from sqlalchemy import Column, Integer, Boolean
from sqlalchemy import String


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
