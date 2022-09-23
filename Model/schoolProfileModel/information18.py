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
    noSubjectPerWeek=Column(Integer,nullable=True)
    noMoralTeachPerWeek=Column(Integer,nullable=True)
    teachingDuration=Column(Integer,nullable=True)
    noHoursForActivity=Column(Integer,nullable=True)
    fromTimeInSummer=Column(TIME,nullable=True)
    toTimeInSummer=Column(TIME,nullable=True)
    fromTimeInWinter=Column(TIME,nullable=True)
    toTimeInWinter=Column(TIME,nullable=True)
    schoolWorkWithShift=Column(String,nullable=True)
    