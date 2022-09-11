import random
from fastapi import Depends,HTTPException,status ,APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from dbconnect import db
from schema import schema
from auth import auth, encrypt
from model import model

root = APIRouter(
    tags=['User']
)

#registration API    
@root.post('/register')
def register(data:schema.registers,db:Session=Depends(db.get_db)):
    user=db.query(model.user).filter(model.user.username == data.username).first()
    if user:
        return {"msg":"try with another username"}
    else :
        mail=db.query(model.user).filter(model.user.email == data.email).first()
        if mail:
            return {"msg":"Already register with this mail Id. try with another one"}
    
    enc=encrypt.hash(data.password)
    data.password=enc
    new_data=model.user(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {"status":"Success"}

        
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Sign up!")        
    
#test api for get current user
@root.get('/get')
def check(db:Session=Depends(db.get_db) ,current_user = Depends(auth.current_user)):
    # data=db.query(model.user).all()
    return current_user

#get all user name
@root.get('/getUser')
def getUser(db:Session = Depends(db.get_db) , current_user = Depends(auth.current_user)):
    check = db.query(model.user).filter(model.user.id == current_user.id , model.user.role == current_user.role).first()
    if check.role ==2 :
       user = db.query(model.user.username,model.user.name,model.user.role).filter(model.user.name !="ADMIN").all()
    else :
        return {"You are not admin"}   
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
                return {"data":data,"msg":"This mail id already registered"}         
    elif all.username != data.username:
        user=db.query(model.user).filter(model.user.username != all.username).all()
        for val in user:
            if data.username == val.username:
                return {"msg":"Try with another username"}
    old_data=db.query(model.user).filter(model.user.id == current_user.id)
    
    if old_data.first():
        old_data.update(data.dict(),synchronize_session=False)
        db.commit()
        data = old_data.first()
        return data
    
 #delete user   
@root.delete("/delete")
def delete(db : Session = Depends(db.get_db) , current_user = Depends(auth.current_user)):
        old_data = db.query(model.user).filter(model.user.id == current_user.id)
        if not old_data.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="User not found")
        old_data.delete(synchronize_session=False)
        db.commit()
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT , detail="Deleted successfully")
        
#change password    
@root.post('/pwd')
def pwdchg(password : schema.pwds , db:Session=Depends(db.get_db), current_user = Depends(auth.current_user)):
    if password.oldPwd == password.newPwd :
        return {"status":2}
    get = db.query(model.user).filter(model.user.id == current_user.id)
    decode = encrypt.check(password.oldPwd ,get.first().password)
    if not decode:
        return {"status":0}
    else:
        encode = encrypt.hash(password.newPwd)
        get.update({"password":encode},synchronize_session=False)
        db.commit()
        return {"status":1}
    
#generate pin
@root.post('/pinGenerate')
def Generate(data:dict, db:Session=Depends(db.get_db)):
    get = db.query(model.user).filter(model.user.username ==data['username']).first()
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Username not exists")
    global pin
    pin=random.randint(123456,999999)
    print(pin)
    return {"pin":pin}    
    
#forgot password
@root.post('/forgotPwd')
def forgotPwd(data:schema.ForgotPwd ,db:Session=Depends(db.get_db)):
        try:
            print(pin)
        except:    
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Refresh the page !")
        
        if data.pin != pin:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid pin")
        find = db.query(model.user).filter(model.user.username == data.username)
        if not find.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Username not exists ,Please Register")
        enPwd = encrypt.hash(data.pwd)
        find.update({"password" : enPwd } , synchronize_session=False)
        db.commit()
        return {"status":"successfully changed"}
            

#change Role:
@root.post('/change' )
def change(data:schema.change , db:Session=Depends(db.get_db)):
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
                    return {"status":"admin created"}
                else:
                    return {"status":f"{user.name} change to Admin"}
            return {"status":f"{user.name} change to User"}
        else :
            return {"status":"user not found"}
    except Exception as error:
        print(error)
        return {"status":"something wrong"}