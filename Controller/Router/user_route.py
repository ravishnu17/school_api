import random
from fastapi import Depends,HTTPException,status ,APIRouter , Response
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from DataBase import db
from Schema import schema
from Authorization import auth
from Model import schoolProfileClass, userClass
from Configuration.config import setting
from Utils import encrypt

root = APIRouter(
    tags=['User']
)

#registration API    
@root.post('/register',status_code=status.HTTP_201_CREATED)
def register(data:schema.registers, response : Response,db:Session=Depends(db.get_db)):
    check_username=db.query(userClass.User).filter(userClass.User.username == data.username).first()
    if check_username:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="Username is unavailable")
    else :
        check_mail=db.query(userClass.User).filter(userClass.User.email == data.email).first()
        if check_mail:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="Already register with this mail Id. try with another one")
    
    #encrypt user password
    encrypt_password=encrypt.hash(data.password)
    data.password=encrypt_password
    
    #insert user data to user table
    insert_user_data=userClass.User(**data.dict())
    db.add(insert_user_data)
    db.commit()
    db.refresh(insert_user_data)
    
    #insert user id to school profile tables
    insert_profile1 = schoolProfileClass.SchoolProfile1(user_id=insert_user_data.id , username = insert_user_data.username)
    insert_profile2 = schoolProfileClass.SchoolProfile2(user_id=insert_user_data.id , username = insert_user_data.username)
    db.add(insert_profile1,insert_profile2)
    db.commit()
    
    return {'email':insert_user_data.email,'status':'success'}

        
#login api
@root.post("/login")
def login(data:OAuth2PasswordRequestForm = Depends() ,db:Session=Depends(db.get_db)):  
    check_credential=db.query(userClass.User).filter(userClass.User.username==data.username).first()
    if check_credential :     
        verify=encrypt.check(data.password,check_credential.password)
        if verify:
            token_data = auth.create_token(data={"id":check_credential.id,"role":check_credential.role , "name":check_credential.name})
            return {"access_token":token_data , "token_type":"bearer" , "role":check_credential.role ,'status':'success' }       
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")        
    
#test api for get current user
@root.get('/get')
def check(db:Session=Depends(db.get_db) ,current_user = Depends(auth.current_user)):
    # data=db.query(model.user).all()
    return current_user

#get all user name  by admin
@root.get('/getUser')
def getUser(response:Response , db:Session = Depends(db.get_db), current_user = Depends(auth.current_user)):
    check_user = db.query(userClass.User).filter(userClass.User.id == current_user.id , userClass.User.role == current_user.role).first()
    if check_user.role ==setting.role and current_user.role == setting.role :
       user = db.query(userClass.User.id, userClass.User.username,userClass.User.name,userClass.User.role).filter(userClass.User.name !="core" , userClass.User.role != current_user.role).all()
    else :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Unauthorized operation")
    return user

#get user details
@root.get('/profile',response_model=schema.responses)
def profile(db:Session=Depends(db.get_db) , current_user = Depends(auth.current_user)):
    data=db.query(userClass.User).filter(userClass.User.id == current_user.id).first()
    return data

#update user detail
@root.post('/profileUpdate')
def update(data:schema.updates,db:Session=Depends(db.get_db),current_user = Depends(auth.current_user)):
    get_user_data=db.query(userClass.User).filter(userClass.User.id == current_user.id).first()
    if get_user_data.email != data.email: 
        user=db.query(userClass.User).filter(userClass.User.email != get_user_data.email).all()
        for val in user:
            if data.email == val.email:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Already registered with this mail ID")        
    
    if get_user_data.username != data.username:
        user=db.query(userClass.User).filter(userClass.User.username != get_user_data.username).all()
        for val in user:
            if data.username == val.username:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Username Already taken ! Try another") 
    
    old_data=db.query(userClass.User).filter(userClass.User.id == current_user.id)
    if old_data.first():
        old_data.update(data.dict(),synchronize_session=False)
        db.commit()
        data = old_data.first()
        return {"data":data , "status":"success"}
    
 #delete user   
@root.delete("/delete")
def delete( db : Session = Depends(db.get_db) , current_user = Depends(auth.current_user)):
        get_user = db.query(userClass.User).filter(userClass.User.id == current_user.id)
        if not get_user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="User not found")
        get_user.delete(synchronize_session=False)
        db.commit()
        return {"status":"deleted successfully"}
        
@root.delete("/deleteID/{id}")
def delete(id, db : Session = Depends(db.get_db) , current_user = Depends(auth.current_user)):
        owner = db.query(userClass.User).filter(userClass.User.id == current_user.id).first()
        if owner.role == setting.role and current_user.role == setting.role:
            data = db.query(userClass.User).filter(userClass.User.id == id)
            if not data.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="User not found")
            data.delete(synchronize_session=False)
            db.commit()
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Not allowed to delete")    
        return {"status":"deleted successfully"}
    
#change password    
@root.post('/password')
def pwdchg(password : schema.pwds , response :Response , db:Session=Depends(db.get_db), current_user = Depends(auth.current_user)):
    if password.oldPwd == password.newPwd :
        response.status_code=status.HTTP_406_NOT_ACCEPTABLE
        return {"status":0 ,"detail":"old and new password should not be same"}
    get = db.query(userClass.User).filter(userClass.User.id == current_user.id)
    
    decode = encrypt.check(password.oldPwd ,get.first().password)
    if not decode:
        response.status_code=status.HTTP_403_FORBIDDEN
        return {"status":1, "detail":"old password is incorrect"}
    else:
        encode = encrypt.hash(password.newPwd)
        get.update({"password":encode},synchronize_session=False)
        db.commit()
        response.status_code=status.HTTP_202_ACCEPTED
        return {"status":2 , "detail":"password changed"}

global key
key= []   
#generate pin
@root.post('/pinGenerate')
def Generate(data:dict, db:Session=Depends(db.get_db)):
    get_user = db.query(userClass.User).filter(userClass.User.username ==data['username']).first()
    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Username not exists")
    
    pin=random.randint(123456,999999)
    index=-1
    if key !=[]:
        for i in range(key.index(key[-1])+1):
            if key[i]['username'] == data['username']:
                index=i
                
        if index !=-1:
            key[index]['pin']=pin
        else:
            val={"username":get_user.username,"pin":pin}
            key.append(val)      
    else:
        val={"username":get_user.username,"pin":pin}
        key.append(val)
                
    return key   
    
#forgot password
@root.post('/forgotPassword')
def forgotPwd(data:schema.ForgotPwd ,db:Session=Depends(db.get_db)):
    find_user = db.query(userClass.User).filter(userClass.User.username == data.username)
    if not find_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Username not exists ,Please Register")       
    
    try:
        for i in range(key.index(key[-1])+1):
            if data.username == key[i]['username']:
                pin =key[i]['pin']
                
    except:    
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT,detail="Refresh the page !")
 
    if data.pin != pin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid pin")
    
    enPwd = encrypt.hash(data.pwd)
    find_user.update({"password" : enPwd } , synchronize_session=False)
    db.commit()
    return {"status":"successfully changed"}
            

#change Role:
@root.post('/changeRole' )
def change(data:schema.change ,response:Response , db:Session=Depends(db.get_db) , current_user = Depends(auth.current_user)):
    if current_user.role ==setting.role:
        try:
            get = db.query(userClass.User).filter(userClass.User.username == data.username)
            if get.first():
                user = get.first()
                get.update(data.dict(), synchronize_session=False)
                db.commit()
                if data.role == 1:
                        return {"status":f"{user.name} change to Admin"}
                return {"status":f"{user.name} change to User"}
            else :
                response.status_code = status.HTTP_404_NOT_FOUND
                return {"status":"user not found"}
        except Exception as error:
            print(error)
            raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED , detail="Something went wrong!")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Unauthorized operation")    
    