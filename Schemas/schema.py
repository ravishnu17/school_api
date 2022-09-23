from datetime import date,time
from typing import Optional
from pydantic import BaseModel,EmailStr

class login(BaseModel):
    username :str
    password :str 

class registers(BaseModel):
    name:str
    dob:date
    gender:str
    mobile:int
    email:EmailStr
    username:str
    password:str
    role:Optional[int]=0
    district:str    
    class Config:
        orm_mode=True
        
class updates(BaseModel):
    name:str
    dob:date
    gender:str
    mobile:int
    email:EmailStr
    username:str
    district:str    
    class Config:
        orm_mode=True  

class pwds(BaseModel):
    oldPwd:str
    newPwd:str              
        
class responses(BaseModel):
    name:str
    dob:date
    role:int
    gender:str
    mobile:int
    email:str
    username:str
    district:str  
    role : int  
    class Config:
        orm_mode=True
        
class change(BaseModel):
    username :str
    role:int         

class token(BaseModel):
    id :Optional[int] = None
    role : Optional[int] = None  
    name : Optional[str] = None    
    
class ForgotPwd(BaseModel):
    username:str
    pin:int
    pwd:str            
    
# class scholar(BaseModel):
#     scholarshipName:str
#     scholarshipBoys: int
#     scholarshipGirls:int
#     Govtscholarship:str
#     Pvtscholarship:str

# class Shift(BaseModel):
#     shiftName:str
#     shiftFromDate: date
#     shiftToDate:date
#     shiftFromTime:time
#     shiftToTime:time
#     shiftRemark:str         