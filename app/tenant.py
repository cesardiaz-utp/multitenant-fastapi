
from typing import Annotated
from fastapi import Depends, HTTPException
from sqlalchemy.sql import text
from sqlalchemy.orm import Session

from app.database import get_default_db

def tenants_info():
    db = next(get_default_db())
    query = "SELECT nombre, base_de_datos FROM clientes"
    print(text(query))
    results = db.execute(statement=text(query)).all()
    # if results == None or len(results) == 0:
    #     raise HTTPException(status_code=404, detail="No hay clientes registrados")
    return [( result[0], result[1] ) for result in results ]