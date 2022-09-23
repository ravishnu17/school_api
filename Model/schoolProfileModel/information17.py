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
    academicYearStart=Column(String,nullable=True)
    academicYearEnd=Column(String,nullable=True)
    noWorkingDays1=Column(Integer,nullable=True)
    noWorkingDays2=Column(Integer,nullable=True)
    noWorkingDays3=Column(Integer,nullable=True)
    noWorkingHours1=Column(Integer,nullable=True)
    noWorkingHours2=Column(Integer,nullable=True)
    noWorkingHours3=Column(Integer,nullable=True)
    totalHours1=Column(Integer,nullable=True)
    totalHours2=Column(Integer,nullable=True)
    totalHours3=Column(Integer,nullable=True)
    noWorkingDaysForStaff1=Column(Integer,nullable=True)
    noWorkingDaysForStaff2=Column(Integer,nullable=True)
    noWorkingDaysForStaff3=Column(Integer,nullable=True)
    noHolidays1=Column(Integer,nullable=True)
    noHolidays2=Column(Integer,nullable=True)
    noHolidays3=Column(Integer,nullable=True)
    