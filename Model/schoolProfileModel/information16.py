from sqlalchemy import Column, Integer,String ,Boolean , TIME ,Date,BigInteger,ForeignKey, ARRAY
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from Model.userModel.user import Base,User

from sqlalchemy.orm import relationship
    
class SchoolProfile(Base):
    __tablename__ = "SchoolProfile"
    owner = relationship('User')
    
    id=Column(Integer,primary_key=True,nullable=False)
    user_id=Column(Integer,ForeignKey("user_data.id",ondelete="CASCADE"), nullable=False)
    username = Column(String,nullable=True , unique=True)
    noCurricularActivities=Column(Integer,nullable=True)
    noGroupsPresent=Column(Integer,nullable=True)
    noCommunityService=Column(Integer,nullable=True)
    schoolSports=Column(Integer,nullable=True)
    zonalSports=Column(Integer,nullable=True)
    districtSports=Column(Integer,nullable=True)
    stateSports=Column(Integer,nullable=True)
    nationalSports=Column(Integer,nullable=True)
    internationalSports=Column(Integer,nullable=True)
    schoolCompetition=Column(Integer,nullable=True)
    zonalCompetition=Column(Integer,nullable=True)
    districtCompetition=Column(Integer,nullable=True)
    stateCompetition=Column(Integer,nullable=True)
    nationalCompetition=Column(Integer,nullable=True)
    internationalCompetition=Column(Integer,nullable=True)
    schoolProgram=Column(Integer,nullable=True)
    zonalProgram=Column(Integer,nullable=True)
    districtProgram=Column(Integer,nullable=True)
    stateProgram=Column(Integer,nullable=True)
    nationalProgram=Column(Integer,nullable=True)
    internationalProgram=Column(Integer,nullable=True)
    