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
    establishYear=Column(String,nullable=True)
    schoolLevel=Column(ARRAY(String),nullable=True)
    medium=Column(ARRAY(String),nullable=True)
    affiliationNature=Column(String,nullable=True)
    teachingStaff=Column(Integer,nullable=True)
    gender=Column(String,nullable=True)
    noGirls=Column(Integer,nullable=True)
    noBoys=Column(Integer,nullable=True)
    totalStudent=Column(Integer,nullable=True)
    nonTeachingStaff=Column(Integer,nullable=True)
    correspondentName=Column(String,nullable=True)
    correspondentMobileNo=Column(BigInteger,nullable=True)
    correspondentMailId=Column(String,nullable=True)
    principalName=Column(String,nullable=True)
    principalMailId=Column(String,nullable=True)
    principalOfficeMobileNo=Column(BigInteger,nullable=True)
    principalMobileNo=Column(BigInteger,nullable=True)
   