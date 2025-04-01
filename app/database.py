from typing import Annotated
from fastapi import Depends, HTTPException, Header
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app.tenant import tenants_info

Base = declarative_base()

def get_database_url(tenant: Annotated[str | None, Header()] = None):
    print(tenant)
    info = tenants_info(tenant)
    if info is not None and len(info) > 0:
        database_url = tenants_info(tenant)[1]
    else:
        raise HTTPException(status_code=404, detail="El cliente solicitado no existe")
    return database_url


def get_db(tenant_db: str = Depends(get_database_url)):
    engine = create_engine(tenant_db)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()