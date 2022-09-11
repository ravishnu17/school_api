from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .path import login,schoolProfile
from model import model
from dbconnect import db
from sqlalchemy import select , insert
from auth import encrypt

model.Base.metadata.create_all(bind=db.engine)

query = select(model.user.username).where(model.user.username == "ADMIN@ADMIN")
with db.engine.connect() as connect:
    data = None
    for row in connect.execute(query):
        data=row
        print(row)
    if not data:
        connect.execute(insert(model.user),{"name":"ADMIN","gender":"male","dob":"17-07-2002","mobile":1234567890,"email":"admin@admin.com","username":"ADMIN@ADMIN","password":encrypt.hash("ADMIN@ADMIN"),"role":2,"district":"krishnagiri"})
        
root=FastAPI()

root.include_router(login.root)
root.include_router(schoolProfile.root)

origins = [
    "http://localhost:4200"
]
root.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]    
)
    
