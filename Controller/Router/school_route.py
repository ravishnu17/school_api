from fastapi import Depends,HTTPException,status ,APIRouter
from sqlalchemy.orm import Session
from typing import List
from Model.schoolProfileModel import schoolProfile
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
    
    return {'Information1':
        {
            'institutionName':get.institutionName , 'postalAddress':get.postalAddress, 'district':get.district, 'state':get.state, 'cityVillageTown':get.cityVillageTown, 'pincode':get.pincode, 'url':get.url, 'officeMail':get.officeMail, 'officeMobile':get.officeMobile, 'schoolLocation':get.schoolLocation ,'childNeeds':get.childNeeds, 'academicYear':get.academicYear
        },
        'Information2':
        {
            "affiliationNature":get.affiliationNature,'correspondentMailId':get.correspondentMailId,'correspondentMobileNo':get.correspondentMobileNo,'correspondentName':get.correspondentName,'establishYear':get.establishYear,'gender':get.gender,'medium':get.medium ,'noBoys':get.noBoys,'noGirls':get.noGirls,'nonTeachingStaff':get.nonTeachingStaff ,'principalMailId':get.principalMailId , 'principalMobileNo':get.principalMobileNo,'principalName':get.principalName,'principalOfficeMobileNo':get.principalOfficeMobileNo,'schoolLevel':get.schoolLevel , 'teachingStaff':get.teachingStaff , 'totalStudent':get.totalStudent
        },
        
        'Information3':
        {
            'recognizedByGovern':get.recognizedByGovern,'boardName':get.boardName ,'affiliationNumber':get.affiliationNumber,'affiliationYear':get.affiliationYear,'affiliationType':get.affiliationType,'affiliationStatement':get.affiliationStatement,'christian':get.christian,'hindu':get.hindu , 'islam':get.islam,'others':get.others,'nonBeliver':get.nonBeliver,'fire':get.fire,'sanitation':get.sanitation,'building':get.building , 'minority':get.minority \
        },
        
        'Information4':
        {
            'schoolOwned':get.schoolOwned,'boardName':get.boardName ,'trustName':get.trustName,'trustRegistered':get.trustRegistered,'registeredAct':get.registeredAct,'registerYear':get.registerYear,'registerNo':get.registerNo,'registrationValidity':get.registrationValidity , 'presidentName':get.presidentName,'presidentDesignation':get.presidentDesignation,'presidentAddress':get.presidentAddress,'presidentNumber':get.presidentNumber,'presidentEmail':get.presidentEmail
        },
        
        'Information5':
        {
            'governingTrust':get.governingTrust , 'governingMember':get.governingMember,'governingTenure':get.governingTenure,
            'educativeCommunity':get.educativeCommunity,
            'educativeCommunityMember':get.educativeCommunityMember,
            'educativeCommunityTenure':get.educativeCommunityTenure,
            'pta':get.pta,'ptaMember':get.ptaMember,'ptaTenure':get.ptaTenure
        },
        
        'Information6':
        {
            'studentCouncil':get.studentCouncil,'studentMember':get.studentMember,'studentTenure':get.studentTenure,'generalComplaint':get.generalComplaint,'schoolCommit':get.schoolCommit,'constitutionCommit':get.constitutionCommit,'constitutionMember':get.constitutionMember,'constitutionTenure':get.constitutionTenure
        },
        
        'Information7':
        {
            'schoolBuilding':get.schoolBuilding,'schoolArea':get.schoolArea,'schoolBuilt':get.schoolBuilt,'groundArea':get.groundArea,'noBuilding':get.noBuilding,'provision':get.provision,'noStaircase':get.noStaircase,'noLift':get.noLift
        },
        
        'Information8':
        {'schoolHistory':get.schoolHistory},
        
        'Information9':{'schoolPlan':get.schoolPlan},
        
        'Information10':
        {
            'classRoom':get.classRoom,'staffRoom':get.staffRoom,'physicalLab':get.physicalLab,'chemistryLab':get.chemistryLab,'biologylab':get.biologylab,'mathsLab':get.mathsLab,'scienceLab':get.scienceLab,'library':get.library,'auditorium':get.auditorium,'counselor':get.counselor,'parlor':get.parlor,'prayer':get.prayer,'sick':get.sick,'canteen':get.canteen,'security':get.security,'otherRoom':get.otherRoom,'staffToilets':get.staffToilets,'studToilet':get.studToilet,'teacher':get.teacher
        },
        
        'Information11':
        {
            'boundryWall':get.boundryWall,'boundryWallStatus':get.boundryWallStatus,'cctv':get.cctv,'dataSave':get.dataSave,'noCamera':get.noCamera,'maleGuard':get.maleGuard,'noMaleGuard':get.noMaleGuard,'femaleGuard':get.noFemaleGuard,'drinkWater':get.drinkWater,'drainage':get.drainage
        },
        
        'Information12':
        {
            'middayScheme':get.middayScheme,'noOwnBus':get.noOwnBus,'gpsCamera':get.gpsCamera,'noladyAttend':get.noladyAttend,'firstAid':get.firstAid,'noDrinkWater':get.noDrinkWater,'BusContract':get.BusContract,'buspass':get.buspass,'freeTransport':get.freeTransport
        },
        
        'Information13':
        {
            'libraryOpenTime':get.libraryOpenTime,'libraryCloseTime':get.libraryCloseTime,'noBook':get.noBook,'noMagazine':get.noMagazine,'noNews':get.noNews,'noEbook':get.noEbook,'primaryLibrary':get.primaryLibrary,'remedial':get.remedial,'tv':get.tv,'digitalboard':get.digitalboard,'computer':get.computer,'projector':get.projector,'tape':get.tape
        },
        
        'Information14':
        {
            'permanentPrincipalMale':get.permanentPrincipalMale,'permanentPrincipalFemale':get.permanentPrincipalFemale,'temporaryPrincipalMale':get.temporaryPrincipalMale,'temporaryPrincipalFemale':get.temporaryPrincipalFemale,'permanentVicePrincipalMale':get.permanentVicePrincipalMale,'permanentVicePrincipalFemale':get.permanentVicePrincipalFemale,'temporaryVicePrincipalMale':get.temporaryVicePrincipalMale,'temporaryVicePrincipalFemale':get.temporaryVicePrincipalFemale,'permanentPGTMale':get.permanentPGTMale,'permanentPGTFemale':get.permanentPGTFemale,'temporaryPGTMale':get.temporaryPGTMale,'temporaryPGTFemale':get.temporaryPGTFemale,'permanentTGTMale':get.permanentTGTMale,'permanentTGTFemale':get.permanentTGTFemale,'temporaryTGTMale':get.temporaryTGTMale,'temporaryTGTFemale':get.temporaryTGTFemale,'permanentPRTMale':get.permanentPRTMale,'permanentPRTFemale':get.permanentPRTFemale,'temporaryPRTMale':get.temporaryPRTMale,'temporaryPRTFemale':get.temporaryPRTFemale,'permanentNTTMale':get.permanentNTTMale,'permanentNTTFemale':get.permanentNTTFemale,'temporaryNTTMale':get.temporaryNTTMale,'temporaryNTTFemale':get.temporaryNTTFemale,'permanentUntrainedTeacherMale':get.permanentUntrainedTeacherMale,'permanentUntrainedTeacherFemale':get.permanentUntrainedTeacherFemale,'temporaryUntrainedTeacherMale':get.temporaryUntrainedTeacherMale,'temporaryUntrainedTeacherFemale':get.temporaryUntrainedTeacherFemale,'permanentLibrarianMale':get.permanentLibrarianMale,'permanentLibrarianFemale':get.permanentLibrarianFemale,'temporaryLibrarianMale':get.temporaryLibrarianMale,'temporaryLibrarianFemale':get.temporaryLibrarianFemale,'permanentMusicTeacherMale':get.permanentMusicTeacherMale,'permanentMusicTeacherFemale':get.permanentMusicTeacherFemale,'temporaryMusicTeacherMale':get.temporaryMusicTeacherMale,'temporaryMusicTeacherFemale':get.temporaryMusicTeacherFemale,'permanentCounsellorMale':get.permanentCounsellorMale,'permanentCounsellorFemale':get.permanentCounsellorFemale,'temporaryCounsellorMale':get.temporaryCounsellorMale,'temporaryCounsellorFemale':get.temporaryCounsellorFemale,'permanentComputerLiteracyMale':get.permanentComputerLiteracyMale,'permanentComputerLiteracyFemale':get.permanentComputerLiteracyFemale,'temporaryComputerLiteracyMale':get.temporaryComputerLiteracyMale,'temporaryComputerLiteracyFemale':get.temporaryComputerLiteracyFemale,'permanentFaithMinisterMale':get.permanentFaithMinisterMale,'permanentFaithMinisterFemale':get.permanentFaithMinisterFemale,'temporaryFaithMinisterMale':get.temporaryFaithMinisterMale,'temporaryFaithMinisterFemale':get.temporaryFaithMinisterFemale,'permanentNurseMale':get.permanentNurseMale,'permanentNurseFemale':get.permanentNurseFemale,'temporaryNurseMale':get.temporaryNurseMale,'temporaryNurseFemale':get.temporaryNurseFemale,'permanentPTTeacherMale':get.permanentPTTeacherMale,'permanentPTTeacherFemale':get.permanentPTTeacherFemale,'temporaryPTTeacherMale':get.temporaryPTTeacherMale,'temporaryPTTeacherFemale':get.temporaryPTTeacherFemale,
        },
        
        'Information15':
        {
          'permanentOfficeManager':get.permanentOfficeManager,'temporaryOfficeManager':get.temporaryOfficeManager,'partTimeOfficeManager':get.partTimeOfficeManager,'permanentOfficeAssistant':get.permanentOfficeAssistant,'temporaryOfficeAssistant':get.temporaryOfficeAssistant,'partTimeOfficeAssistant':get.partTimeOfficeAssistant,'permanentClerk':get.permanentClerk,'temporaryClerk':get.temporaryClerk,'partTimeClerk':get.partTimeClerk,'permanentLabAttendants':get.permanentLabAttendants,'temporaryLabAttendants':get.temporaryLabAttendants,'partTimeLabAttendants':get.partTimeLabAttendants,'permanentAccountant':get.permanentAccountant,'temporaryAccountant':get.temporaryAccountant,'partTimeAccountant':get.partTimeAccountant,'permanentPeonesClerk':get.permanentPeonesClerk,'temporaryPeonesClerk':get.temporaryPeonesClerk,'partTimePeonesClerk':get.partTimePeonesClerk,'permanentOthers':get.permanentOthers,'temporaryOthers':get.temporaryOthers,'partTimeOthers':get.partTimeOthers
        },
        
        'Information16':
        {
            'noCurricularActivities':get.noCurricularActivities,'noGroupsPresent':get.noGroupsPresent,'noCommunityService':get.noCommunityService,'schoolSports':get.schoolSports,'zonalSports':get.zonalSports,'districtSports':get.districtSports,'stateSports':get.stateSports,'nationalSports':get.nationalSports,'internationalSports':get.internationalSports,'schoolCompetition':get.schoolCompetition,'zonalCompetition':get.zonalCompetition,'districtCompetition':get.districtCompetition,'stateCompetition':get.stateCompetition,'nationalCompetition':get.nationalCompetition,'internationalCompetition':get.internationalCompetition,'schoolProgram':get.schoolProgram,'zonalProgram':get.zonalProgram,'districtProgram':get.districtProgram,'stateProgram':get.stateProgram,'nationalProgram':get.nationalProgram,'internationalProgram':get.internationalProgram
        },
        
        'Information17':
        {
            'academicYearStart':get.academicYearStart,'academicYearEnd':get.academicYearEnd,'noWorkingDays1':get.noWorkingDays1,'noWorkingDays2':get.noWorkingDays2,'noWorkingDays3':get.noWorkingDays3,'noWorkingHours1':get.noWorkingHours1,'noWorkingHours2':get.noWorkingHours2,'noWorkingHours3':get.noWorkingHours3,'totalHours1':get.totalHours1,'totalHours2':get.totalHours2,'totalHours3':get.totalHours3,'noWorkingDaysForStaff1':get.noWorkingDaysForStaff1,'noWorkingDaysForStaff2':get.noWorkingDaysForStaff2,'noWorkingDaysForStaff3':get.noWorkingDaysForStaff3,'noHolidays1':get.noHolidays1,'noHolidays2':get.noHolidays2,'noHolidays3':get.noHolidays3,
        },
        
        'Information18':
        {
            'noSubjectPerWeek':get.noSubjectPerWeek,'noMoralTeachPerWeek':get.noMoralTeachPerWeek,'teachingDuration':get.teachingDuration,'noHoursForActivity':get.noHoursForActivity,'fromTimeInSummer':get.fromTimeInSummer,'toTimeInSummer':get.toTimeInSummer,'fromTimeInWinter':get.fromTimeInWinter,'toTimeInWinter':get.toTimeInWinter,'schoolWorkWithShift':get.schoolWorkWithShift
        },
        
        'Information19':{'scholarship':get.scholarship},
        
        'Information20':{'shift':get.shift,'schoolClass':get.schoolClass},
        
        }
    
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