from itertools import count
from re import A
from fastapi import Depends,HTTPException,status ,APIRouter
from sqlalchemy.orm import Session
# from ..import model,schema,db,auth
from typing import List
from model import model
from dbconnect import db
from auth import auth

root=APIRouter(
    tags=['School Profile']
)

# def getDynamic(data):
    # if index==0:
    #     keys=["scholarshipName","scholarshipBoys","scholarshipGirls","Govtscholarship","Pvtscholarship"]
    # elif index==1:
    #     keys=["shiftName","shiftFromDate","shiftToDate","shiftFromTime","shiftToTime","shiftRemark"]
    # elif index ==2:
    #     keys = ["className","classSection","classBoys","classGirls","classStudent"] 
    # keys=['id','text']
    # get={}
    # set=[]
    # for list in data:
    #     for i in range(list.index(list[-1])+1):
    #         get.update({keys[i]:list[i]})
    #     set.append(get)
    #     get={}   
    # return set

      
#get school profile details    
@root.get('/SchoolProfile')
def getSchoolProfile(db:Session=Depends(db.get_db) , current_user = Depends(auth.current_user)):
    get = db.query(model.schoolProfile).filter(model.schoolProfile.user_id == current_user.id).first()
    # get.level = getDynamic(get.level)
    return get
    
#convert dict to list   
def setDynamic(data):
    #store
    getKey:list=[] 
    get:list=[]
    set:list=[]
    for list in data:
        for keys in list:
            getKey.append(keys)       
        break    
    
    for list in data:
        for load in getKey:
            get.append(list[load])
        set.append(get)
        get=[] 
    return set        
        
#update school profile details    
@root.post('/schoolUpdate')
def UpdateSchool(data : dict , db:Session=Depends(db.get_db) ,  current_user = Depends(auth.current_user)):
    get = db.query(model.schoolProfile).filter(model.schoolProfile.user_id == current_user.id) 
    print(current_user)   
    if data.get('scholarship'):    
        data['scholarship']=setDynamic(data['scholarship'])
    if data.get('shift'):
        data['shift']=setDynamic(data['shift'])
    if data.get('schoolClass'):
        data['schoolClass']=setDynamic(data['schoolClass'])
    if data.get('level'):
        data['level']=setDynamic(data['level'])  
    if data.get('medium'):
        data['medium']=setDynamic(data['medium'])        
    try:
        if get.first():
            get.update(data,synchronize_session=False)
            db.commit()
            return {"status" :"Saved successfully"}
        else :
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="You are not admin ! contact the team")    
    except Exception as error :
        print(error)
        return {"status":"error"}    