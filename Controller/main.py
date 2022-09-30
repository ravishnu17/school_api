from fastapi import  FastAPI , Depends
from sqlalchemy.orm import Session
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from .Router import school_route, user_route
from Model.userModel import user
from DataBase import db
from sqlalchemy import select , insert
from Utils import encrypt
from Configuration.config import setting

# model.Base.metadata.create_all(bind=db.engine)
    
query = select(user.User.username).where(user.User.username == setting.adminuser)
with db.engine.connect() as connect:
    data = None
    for row in connect.execute(query):
        data=row
        # print(f'admin - {row}')
    if not data:
        connect.execute(insert(user.User),{"name":"core","gender":"male","dob":"2002-07-17","mobile":1234567890,"email":setting.email,"username":setting.adminuser,"password":encrypt.hash(setting.password),"role":setting.role,"district":"krishnagiri"})

       
root=FastAPI()

root.include_router(user_route.root)
root.include_router(school_route.root)

origins = [
    "https://school-view-manage.herokuapp.com",
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
    
