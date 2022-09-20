def test_getSchoolProfile(AuthClient , TestUser2):
    res = AuthClient.get('/SchoolProfile')
    print(res.json()['institute'])
    assert res.status_code == 200