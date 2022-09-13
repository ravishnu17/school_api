import json
import pytest
from fastapi.testclient import TestClient
from control.main import root
from schema import schema

# client = TestClient(root)

def test_root(client):
    res = client.get("/")
    assert res.status_code == 200
    
def test_register(client ):
    res=client.post("/register",json = {"name":"Ravishnu","dob":"2002-07-17","gender":"male","mobile":"9876504321","email":"ravi@gmail.com","username":"ravi","password":"Ravishnu","district":"Krishnagiri"})
    data = schema.responses(**res.json())
    assert data.email == "ravi@gmail.com"
    assert res.status_code == 201    
 
@pytest.mark.parametrize("username , email , status",[("Ravishnu","ravi12@gmail.com",409),("ravi","ravi@gmail.com",409)])
def test_ivalid_register(client ,testUser, username ,email,status):
    res=client.post("/register",json = {"name":"Ravishnu","dob":"2002-07-17","gender":"male","mobile":"9876504321","email":email,"username":username,"password":"Ravishnu","district":"Krishnagiri"})
    print("\n",res.json()['msg'])
    assert res.status_code == status 

    
def test_login(client , testUser):
    res = client.post("/login",data={"username":testUser['username'],"password":testUser['password']})
    assert res.json()['token_type'] == "bearer"
    assert res.status_code == 200  

@pytest.mark.parametrize("username,password,status_code",[('Ravishnu','Ravi@8610',404),('ravi','ravi',404),('','Ravi@8610',422),('ravi','',422)])
def test_invalid_login(client ,testUser, username , password , status_code):
    res = client.post("/login",data={"username":username,"password":password})        
    print(res.json()['detail'])
    assert res.status_code ==status_code
    