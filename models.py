from sqlalchemy import Column, Integer, String, Float
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)  # admin / analyst / viewer
    is_active = Column(Integer, default=1)


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)
    category = Column(String)
    date = Column(String)
    note = Column(String)
    is_deleted = Column(Integer, default=0)