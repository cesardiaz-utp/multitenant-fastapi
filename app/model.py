
from sqlalchemy import Boolean, Column, Integer, String, SmallInteger
from app.database import Base

class User(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    active = Column(SmallInteger)

class Person(Base):
    __tablename__ = "tercero"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    representative_name = Column(String)
    representative_email = Column(String)
    active = Column(SmallInteger)
