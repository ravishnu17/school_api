def test_getSchoolProfile(AuthClient ):
    res = AuthClient.get('/SchoolProfile')
    print(res.json()['Information1'])
    assert res.status_code == 200
    
def test_updateSchoolProfile(AuthClient):
        res = AuthClient.post('/schoolUpdate',json={'institutionName':'Don Bosco'})
        print(res.json()['status'])
        
        assert res.status_code == 200
        
def test_updateSchoolProfile_unauthorized(Client):
    res = Client.post('/schoolUpdate',json={'institutionName':'Don Bosco'})
    print(res.json()['detail'])
        
    assert res.status_code == 401       
    
def test_updateSchoolProfile_notallowed(AuthClient2):
    res = AuthClient2.post('/schoolUpdate',json={'institutionName':'Don Bosco'})
    print(res.json()['detail'])
        
    assert res.status_code == 403     