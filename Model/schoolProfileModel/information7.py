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
    schoolBuilding=Column(String,nullable=True)
    schoolArea=Column(String,nullable=True)
    schoolBuilt=Column(String,nullable=True)
    groundArea=Column(String,nullable=True)
    noBuilding=Column(Integer,nullable=True)
    provision=Column(Integer,nullable=True)
    noStaircase=Column(Integer,nullable=True)
    noLift=Column(Integer,nullable=True)
    