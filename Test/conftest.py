import pytest
from fastapi.testclient import TestClient
from control.main import root
from config.config import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbconnect.db import get_db,Base
from auth.auth import create_token
from auth import encrypt


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
    
#create test user    
@pytest.fixture
def TestUser(Client):
    userData={"name":"Ravishnu","dob":"2002-07-17","gender":"male","mobile":"9876504321","email":"ravi@gmail.com","username":"Ravishnu","password":encrypt.hash("Ravishnu"),"district":"Krishnagiri"}
    res = Client.post('/register',json=userData)
    user = res.json()
    return user

@pytest.fixture
def TestUser2(Client):
    userData={"name":"Muni","dob":"2002-07-17","gender":"male","mobile":"9876504321","email":"muni@gmail.com","username":"Muni","password":"Muni","district":"Krishnagiri"}
    userData['password']=encrypt.hash(userData['password'])
    res = Client.post('/register',json=userData)
    user = res.json()
    return user

@pytest.fixture
def Token(TestUser2):
    return create_token(data={"id":TestUser2['id'],"role":TestUser2['role'],"name":TestUser2['name']})

@pytest.fixture
def AuthClient(Client , Token):
    Client.headers = {**Client.headers , "Authorization":f"bearer {Token}"}
    return Client


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
