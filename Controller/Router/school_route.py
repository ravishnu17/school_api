from fastapi import Depends,HTTPException,status ,APIRouter
from sqlalchemy.orm import Session
from typing import List
from Model import schoolProfile
from DataBase import db
from Authorization import auth

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
def school_profile_data(db:Session=Depends(db.get_db) , current_user = Depends(auth.current_user)):
    get = db.query(schoolProfile.SchoolProfile).filter(schoolProfile.SchoolProfile.user_id == current_user.id).first()
    # get.level = getDynamic(get.level)
    # return {'generalInformation1':get1 , 'generalInformation2':get2}
    return {'generalInformation1':{'institutionName':get.institutionName , 'postalAddress':get.postalAddress, 'district':get.district, 'state':get.state, 'cityVillageTown':get.cityVillageTown, 'pincode':get.pincode, 'url':get.url, 'officeMail':get.officeMail, 'officeMobile':get.officeMobile, 'schoolLocation':get.schoolLocation ,'childNeeds':get.childNeeds, 'academicYear':get.academicYear},'generalInformation2':{"affiliationNature":get.affiliationNature,'correspondentMailId':get.correspondentMailId,'correspondentMobileNo':get.correspondentMobileNo,'correspondentName':get.correspondentName,'establishYear':get.establishYear,'gender':get.gender,'medium':get.medium ,'noBoys':get.noBoys,'noGirls':get.noGirls,'nonTeachingStaff':get.nonTeachingStaff ,'principalMailId':get.principalMailId , 'principalMobileNo':get.principalMobileNo,'principalName':get.principalName,'principalOfficeMobileNo':get.principalOfficeMobileNo,'schoolLevel':get.schoolLevel , 'teachingStaff':get.teachingStaff , 'totalStudent':get.totalStudent}}
    
#convert dict to list or array   
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
def update_school(data : dict , db:Session=Depends(db.get_db) ,  current_user = Depends(auth.current_user)):
    get_data = db.query(schoolProfile.SchoolProfile).filter(schoolProfile.SchoolProfile.user_id == current_user.id)   
    if data.get('scholarship'):    
        data['scholarship']=setDynamic(data['scholarship'])
    if data.get('shift'):
        data['shift']=setDynamic(data['shift'])
    if data.get('schoolClass'):
        data['schoolClass']=setDynamic(data['schoolClass'])
    if data.get('schoolLevel'):
        data['schoolLevel']=setDynamic(data['schoolLevel'])  
    if data.get('medium'):
        data['medium']=setDynamic(data['medium']) 
    # data['generalInformation1'].update(data['generalInformation2'])
    # print(data)           
    try:
        if get_data.first():
            get_data.update(data,synchronize_session=False)
            db.commit()
            return {"status" :"Saved successfully"}
        else :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="You are not admin ! contact the team")    
    except Exception as error :
        print(error)
        raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED , detail="Try Again!")   