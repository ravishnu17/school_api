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
    institutionName=Column(String,nullable=True)
    postalAddress=Column(String,nullable=True)
    district=Column(String,nullable=True)
    state=Column(String,nullable=True)
    cityVillageTown=Column(String,nullable=True)
    pincode=Column(BigInteger,nullable=True)
    url=Column(String,nullable=True)
    officeMail=Column(String,nullable=True)
    officeMobile=Column(BigInteger,nullable=True)
    schoolLocation=Column(String,nullable=True)
    childNeeds=Column(String,nullable=True)
    academicYear=Column(String,nullable=True)    
    