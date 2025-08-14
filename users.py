from sqlalchemy import Column, Integer, String
from database import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String(50), nullable=False)
    balans = Column(Integer, nullable=False)