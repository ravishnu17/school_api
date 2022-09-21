from fastapi import  FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from .path import user,schoolProfile
from model import model
from dbconnect import db
from sqlalchemy import select , insert
from auth import encrypt
from config.config import setting

# model.Base.metadata.create_all(bind=db.engine)
query = select(model.user.username).where(model.user.username == setting.adminuser)
with db.engine.connect() as connect:
    data = None
    for row in connect.execute(query):
        data=row
        print(f'admin - {row}')
    if not data:
        connect.execute(insert(model.user),{"name":"core","gender":"male","dob":"2002-07-17","mobile":1234567890,"email":setting.email,"username":setting.adminuser,"password":encrypt.hash(setting.password),"role":setting.role,"district":"krishnagiri"})
        
root=FastAPI()

root.include_router(user.root)
root.include_router(schoolProfile.root)

origins = [
    "https://school-design-angular.herokuapp.com",
    "http://localhost:4200"
]
root.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]    
)


@root.get("/")
def gets():
    return {"message":"Hello"}
    
