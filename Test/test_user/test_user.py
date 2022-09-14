import json
import pytest
# from fastapi.testclient import TestClient
from control.main import root
from schema import schema
from auth import encrypt

# client = TestClient(root)

def test_root(Client):
    res = Client.get("/")
    assert res.status_code == 200
    
def test_register(Client ):
    res=Client.post("/register",json = {"name":"Ravishnu","dob":"2002-07-17","gender":"male","mobile":"9876504321","email":"ravi@gmail.com","username":"ravi","password":"Ravishnu","district":"Krishnagiri"})
    print(res.json()['name'])
    assert res.json()['email'] == "ravi@gmail.com"
    assert res.status_code == 201    
 
@pytest.mark.parametrize("username , email , status",[("Ravishnu","ravi12@gmail.com",409),("ravi","ravi@gmail.com",409)])
def test_invalid_register(Client ,TestUser, username ,email,status):
    res=Client.post("/register",json = {"name":"Ravishnu","dob":"2002-07-17","gender":"male","mobile":"9876504321","email":email,"username":username,"password":"Ravishnu","district":"Krishnagiri"})
    print("\n",res.json()['msg'])
    assert res.status_code == status 

    
def test_login(Client , TestUser):
    res = Client.post("/login",data={"username":TestUser['username'],"password":TestUser['password']})
    assert res.json()['token_type'] == "bearer"
    assert res.status_code == 200  

@pytest.mark.parametrize("username,password,status_code",[('Ravishnu','Ravi@8610',404),('ravi','ravi',404),('','Ravi@8610',422),('ravi','',422)])
def test_invalid_login(Client ,TestUser, username , password , status_code):
    res = Client.post("/login",data={"username":username,"password":password})        
    print(res.json()['detail'])
    assert res.status_code ==status_code
    
def test_get_current_user(AuthClient):
    res = AuthClient.get('/get')
    print(res.json()['name'])
    assert res.json()['role']==0
    assert res.json()['name']=='Muni'
    assert res.status_code == 200
    
def test_getAllUser_nonAdmin(AuthClient):
    res = AuthClient.get('/getUser')
    print(res.json()['detail'])
    res.status_code == 401    
    
def test_getAllUser_byAdmin(AdminClient , TestUser , TestUser2):   
    res = AdminClient.get("/getUser")
    
    for i in range(res.json().index(res.json()[-1])+1):
        print(res.json()[i]['name'] ,end=" ")
    assert res.status_code == 200   
    
def test_get_currentUserProfile(AuthClient , TestUser2):
    res = AuthClient.get("/profile")
    assert res.json()['name'] == TestUser2['name']
    print(res.json()['name'])
    assert res.status_code == 200    

@pytest.mark.parametrize("username , email , status",[('Muniraj',"muniraj@gmail.com",200),('Ravishnu','muni@gmail.com',409),('Muni','ravi@gmail.com',409)])
def test_update_currentUserData(AuthClient ,TestUser ,  TestUser2 , username ,email ,status):
    data ={"name":"Muni","dob":"2002-07-17","gender":"male","mobile":"9876504321","email":email,"username":username,"password":"Muni","district":"Krishnagiri"}
    data['password'] = encrypt.hash(data['password'])
    res = AuthClient.post("/profileUpdate" , json=data)   
    print(res.json()['detail'])
    assert res.status_code == status
    
def test_deleteUser(AuthClient):
        res = AuthClient.delete("/delete")
        print(res.json()['detail'])
        assert res.status_code ==200
        
@pytest.mark.parametrize("old,new,status",[('Muni','Muniraj',202),('muni','muni',406),('muni','Muniraj',403)])
def test_changePassword(AuthClient,TestUser2 ,old, new ,status):
    res = AuthClient.post('/pwd',json={"oldPwd":old,"newPwd":new})
    print(res.json()['msg'])
    assert res.status_code == status        