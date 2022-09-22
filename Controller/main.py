from fastapi import  FastAPI , Depends
from sqlalchemy.orm import Session
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from .Router import school_route, user_route
from Model import userClass
from DataBase import db
from sqlalchemy import select , insert
from Utils import encrypt
from Configuration.config import setting

# model.Base.metadata.create_all(bind=db.engine)
    
# query = select(userClass.User.username).where(userClass.User.username == setting.adminuser)
# with db.engine.connect() as connect:
#     data = None
#     for row in connect.execute(query):
#         data=row
#         print(f'admin - {row}')
#     if not data:
        # connect.execute(insert(userClass.User),{"name":"core","gender":"male","dob":"2002-07-17","mobile":1234567890,"email":setting.email,"username":setting.adminuser,"password":encrypt.hash(setting.password),"role":setting.role,"district":"krishnagiri"})

       
root=FastAPI()

root.include_router(user_route.root)
root.include_router(school_route.root)

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
def gets(db:Session=Depends(db.get_db)):
    admin = db.query(userClass.User).filter(userClass.User.username == setting.adminuser).first()
    if not admin:
        AdminData =userClass.User(name='admin',gender='male',dob='c 2002-07-17' , mobile=1234567890,email=setting.email,username=setting.adminuser,password=encrypt.hash(setting.password),role=setting.role,district="krishnagiri")
        db.add(AdminData)
        db.commit()
    else:
        print(admin.username)
    return {"message":"Hello"}
    
