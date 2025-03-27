
from fastapi import FastAPI
from app.routes.users import userR
from app.tenant import tenants_info

app = FastAPI()

app.include_router(userR)

@app.get("/")
async def home():
    return {"message": "Hello World"}

print(tenants_info())