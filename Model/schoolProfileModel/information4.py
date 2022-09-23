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
    schoolOwned=Column(String,nullable=True)
    trustName=Column(String,nullable=True)
    trustRegistered=Column(String,nullable=True)
    registeredAct=Column(String,nullable=True)
    registerYear=Column(Integer,nullable=True)
    registerNo=Column(String,nullable=True)
    registrationValidity=Column(Integer,nullable=True)
    presidentName=Column(String,nullable=True)
    presidentDesignation=Column(String,nullable=True)
    presidentAddress=Column(String,nullable=True)
    presidentNumber=Column(BigInteger,nullable=True)
    presidentEmail=Column(String,nullable=True)
    