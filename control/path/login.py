import random
from fastapi import Depends,HTTPException,status ,APIRouter , Response
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from dbconnect import db
from schema import schema
from auth import auth, encrypt
from model import model
from config.config import setting
root = APIRouter(
    tags=['User']
)

#registration API    
@root.post('/register',status_code=status.HTTP_201_CREATED)
def register(data:schema.registers, response : Response,db:Session=Depends(db.get_db)):
    user=db.query(model.user).filter(model.user.username == data.username).first()
    if user:
        response.status_code=status.HTTP_409_CONFLICT
        return {"msg":"try with another username"}
    else :
        mail=db.query(model.user).filter(model.user.email == data.email).first()
        if mail:
            response.status_code=status.HTTP_409_CONFLICT
            return {"msg":"Already register with this mail Id. try with another one"}
    
    enc=encrypt.hash(data.password)
    data.password=enc
    new_data=model.user(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

        
#login api
@root.post("/login")
def login(data:OAuth2PasswordRequestForm = Depends() ,db:Session=Depends(db.get_db)):  
    login_data=db.query(model.user).filter(model.user.username==data.username).first()
    if login_data :     
        verify=encrypt.check(data.password,login_data.password)
        if verify:
            token_data = auth.create_token(data={"id":login_data.id,"role":login_data.role , "name":login_data.name})
            return {"access_token":token_data , "token_type":"bearer" , "role":login_data.role }       
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")        
    
#test api for get current user
@root.get('/get')
def check(db:Session=Depends(db.get_db) ,current_user = Depends(auth.current_user)):
    # data=db.query(model.user).all()
    return current_user

#get all user name
@root.get('/getUser')
def getUser(response:Response , db:Session = Depends(db.get_db), current_user = Depends(auth.current_user)):
    check = db.query(model.user).filter(model.user.id == current_user.id , model.user.role == current_user.role).first()
    if check.role ==setting.role and current_user.role == setting.role :
       user = db.query(model.user.username,model.user.name,model.user.role).filter(model.user.name !="core" , model.user.role != current_user.role).all()
    else :
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"detail":"You are not admin"}   
    return user

#get detail by id
@root.get('/profile',response_model=schema.responses)
def profile(db:Session=Depends(db.get_db) , current_user = Depends(auth.current_user)):
    data=db.query(model.user).filter(model.user.id == current_user.id).first()
    return data

#update user detail
@root.post('/profileUpdate')
def update(data:schema.updates,db:Session=Depends(db.get_db),current_user = Depends(auth.current_user)):
    all=db.query(model.user).filter(model.user.id == current_user.id).first()
    if all.email != data.email: 
        user=db.query(model.user).filter(model.user.email != all.email).all()
        for val in user:
            if data.email == val.email:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Already registered with this mail ID")        
    
    if all.username != data.username:
        user=db.query(model.user).filter(model.user.username != all.username).all()
        for val in user:
            if data.username == val.username:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Username Already taken ! Try another") 
    
    old_data=db.query(model.user).filter(model.user.id == current_user.id)
    if old_data.first():
        old_data.update(data.dict(),synchronize_session=False)
        db.commit()
        data = old_data.first()
        return {"data":data , "detail":"updated"}
    
 #delete user   
@root.delete("/delete")
def delete( db : Session = Depends(db.get_db) , current_user = Depends(auth.current_user)):
        old_data = db.query(model.user).filter(model.user.id == current_user.id)
        if not old_data.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="User not found")
        old_data.delete(synchronize_session=False)
        db.commit()
        return {"detail":"deleted successfully"}
        
#change password    
@root.post('/pwd')
def pwdchg(password : schema.pwds , response :Response , db:Session=Depends(db.get_db), current_user = Depends(auth.current_user)):
    if password.oldPwd == password.newPwd :
        response.status_code=status.HTTP_406_NOT_ACCEPTABLE
        return {"status":2 ,"msg":"old and new password should not be same"}
    get = db.query(model.user).filter(model.user.id == current_user.id)
    decode = encrypt.check(password.oldPwd ,get.first().password)
    if not decode:
        response.status_code=status.HTTP_403_FORBIDDEN
        return {"status":0 , "msg":"old password is incorrect"}
    else:
        encode = encrypt.hash(password.newPwd)
        get.update({"password":encode},synchronize_session=False)
        db.commit()
        response.status_code=status.HTTP_202_ACCEPTED
        return {"status":1 , "msg":"password changed"}

global key
key= []   
#generate pin
@root.post('/pinGenerate')
def Generate(data:dict, db:Session=Depends(db.get_db)):
    get = db.query(model.user).filter(model.user.username ==data['username']).first()
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Username not exists")
    
    pin=random.randint(123456,999999)
    name=-1
    if key !=[]:
        for i in range(key.index(key[-1])+1):
            if key[i]['username'] == data['username']:
                name=i
                
        if name !=-1:
            key[name]['pin']=pin
        else:
            val={"username":get.username,"pin":pin}
            key.append(val)      
    else:
        val={"username":get.username,"pin":pin}
        key.append(val)
                
    return key   
    
#forgot password
@root.post('/forgotPwd')
def forgotPwd(data:schema.ForgotPwd ,db:Session=Depends(db.get_db)):
    find = db.query(model.user).filter(model.user.username == data.username)
    if not find.first():
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
    find.update({"password" : enPwd } , synchronize_session=False)
    db.commit()
    return {"status":"successfully changed"}
            

#change Role:
@root.post('/change' )
def change(data:schema.change ,response:Response , db:Session=Depends(db.get_db) , current_user = Depends(auth.current_user)):
    role = current_user.role
    if role ==2:
        try:
            get = db.query(model.user).filter(model.user.username == data.username)
            if get.first():
                user = get.first()
                get.update(data.dict(), synchronize_session=False)
                db.commit()
                if data.role == 1:
                    check = db.query(model.schoolProfile).filter(model.schoolProfile.user_id == get.first().id).first()
                    if not check:
                        admin_table = model.schoolProfile(user_id = get.first().id , username = get.first().username)
                        db.add(admin_table)
                        db.commit()
                        db.refresh(admin_table)
                        print(admin_table)
                        response.status_code =status.HTTP_201_CREATED
                        return {"status":"admin created"}
                    else:
                        response.status_code = status.HTTP_200_OK
                        return {"status":f"{user.name} change to Admin"}
                response.status_code = status.HTTP_200_OK
                return {"status":f"{user.name} change to User"}
            else :
                response.status_code = status.HTTP_404_NOT_FOUND
                return {"status":"user not found"}
        except Exception as error:
            print(error)
            raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED , detail="Something went wrong!")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Unauthorized operation")    
    
@root.post('/test')
def check(data:dict):
    print(data)    
    return data