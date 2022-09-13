import pytest
from fastapi.testclient import TestClient
from control.main import root
from config.config import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbconnect.db import get_db,Base


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
    

@pytest.fixture
def client(): 
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
    
@pytest.fixture
def testUser(client):
    userData={"name":"Ravishnu","dob":"2002-07-17","gender":"male","mobile":"9876504321","email":"ravi@gmail.com","username":"Ravishnu","password":"Ravishnu","district":"Krishnagiri"}
    res = client.post('/register',json=userData)
    user = res.json()
    user['password'] = userData['password']
    return user
        