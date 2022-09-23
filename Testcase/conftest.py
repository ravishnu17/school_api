import json
import pytest
from fastapi.testclient import TestClient
from Controller.main import root
from Configuration.config import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DataBase.db import get_db,Base
from Authorization.auth import create_token
from Utils import encrypt
from Model.userModel import user


sql_url = f"postgresql://{setting.db_username}:{setting.db_password}@{setting.db_host}:{setting.db_port}/{setting.db_name}_test"
engine = create_engine(sql_url)
session_test = sessionmaker(autocommit=False , autoflush= False , bind=engine)

# @pytest.fixture
# def session():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     db=SessionLocal_test()
    
#     try:
#         yield db
#     finally:
#         db.close()    
    
#setup test db
@pytest.fixture
def Client(): 
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db=session_test()       
    def getTest_db():
        try:
            yield db
        finally:
            db.close()    
    root.dependency_overrides[get_db]=getTest_db
    yield TestClient(root)
    

#create test Admin
@pytest.fixture
def TestAdmin(Client):    
    userData={"name":"ADMIN","dob":"2002-07-17","gender":"male","mobile":"9876504321","email":"admin@gmail.com","username":"ADMIN@ADMIN","password":encrypt.hash("ADMIN@ADMIN"),"role":2,"district":"Krishnagiri"}
    res = Client.post('/register',json=userData)
    user = res.json()
    
    token = create_token(data={'id':user['id'],"role":user['role'],"name":user['name']})
    return token

@pytest.fixture
def AdminClient(Client , TestAdmin):
    Client.headers = {**Client.headers , "Authorization":f"bearer {TestAdmin}"}
    return Client    
    
#create test user    
@pytest.fixture
def TestUser(Client):
    userData={"name":"Ravishnu","dob":"2002-07-17","gender":"male","mobile":"9876504321","email":"ravi@gmail.com","username":"Ravishnu","password":"Ravishnu","district":"Krishnagiri"}
    res = Client.post('/register',json=userData)
    user = res.json()
    user['password'] = userData['password']
    return user

@pytest.fixture
def TestUser2(Client):
    userData={"name":"Muni","dob":"2002-07-17","gender":"male","mobile":"9876504321","email":"muni@gmail.com","username":"Muni","password":"Muni","district":"Krishnagiri"}
    res = Client.post('/register',json=userData)
    user = res.json()
    user['password'] = userData['password']
    return user

@pytest.fixture
def Token(TestUser2):
    return create_token(data={"id":TestUser2['id'],"role":TestUser2['role'],"name":TestUser2['name']})

@pytest.fixture
def AuthClient(Client , Token):
    Client.headers = {**Client.headers , "Authorization":f"bearer {Token}"}
    return Client


@pytest.fixture
def GetPin(Client , TestUser):
    res = Client.post("/pinGenerate" , json={'username':TestUser['username']})
    return res.json()[0]['pin']

@pytest.fixture
def testSchoolAdmin(AdminClient , TestUser2):
    res = AdminClient.post('/change' , json={'username':TestUser2['username'],'role':1})
    

@pytest.fixture
def testInsertSchool(AuthClient , testSchoolAdmin):
    res = AuthClient.post('/schoolUpdate' , json={'district':'Krishnagiri'})
    print(res.json())
    assert res.status_code == 200