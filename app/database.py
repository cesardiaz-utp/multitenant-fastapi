from typing import Annotated
from fastapi import Depends, Header
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app.config import settings

Base = declarative_base()

def get_database_url(tenant: Annotated[str | None, Header()] = None):
    if tenant == 'tenant1':
        print('tenant1')
        database_url = settings.database_url_1
    elif tenant == 'tenant2':
        print('tenant2')
        database_url = settings.database_url_2
    else:
        print('shared')
        database_url = settings.shared_url
    return database_url


def get_db(tenant_db: str = Depends(get_database_url)):
    engine = create_engine(tenant_db)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

def get_default_db():
    engine = create_engine(get_database_url('shared'))

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
