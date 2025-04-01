
from typing import Annotated
from fastapi import Depends, HTTPException
from sqlalchemy.sql import text
from sqlalchemy.orm import Session

from app.database_shared import get_db

tenants = {}

def _get_info_by_name(name: str = None):
    info = tenants[name] if name in tenants else None
    if info != None:
        return info
    else:
        db = next(get_db())
        query = f"SELECT nombre, base_de_datos FROM clientes WHERE nombre = '{name}'"
        print(query)
        result = db.execute(statement=text(query)).one()
        if result == None or len(result) == 0:
            raise HTTPException(status_code=404, detail=f"El cliente {name} no existe")
        tenants[name] = result
        return result    

def tenants_info(tenant: str = None):
    db = next(get_db())
    if tenant != None:
        return _get_info_by_name(tenant)
    else:
        query = "SELECT nombre, base_de_datos FROM clientes"
        print(query)
        return db.execute(statement=text(query)).all()
