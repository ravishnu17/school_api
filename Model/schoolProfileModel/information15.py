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
    permanentOfficeManager = Column(Integer,nullable=True)
    temporaryOfficeManager = Column(Integer,nullable=True)
    partTimeOfficeManager = Column(Integer,nullable=True)
    permanentOfficeAssistant = Column(Integer,nullable=True)
    temporaryOfficeAssistant = Column(Integer,nullable=True)
    partTimeOfficeAssistant = Column(Integer,nullable=True)
    permanentClerk = Column(Integer,nullable=True)
    temporaryClerk = Column(Integer,nullable=True)
    partTimeClerk = Column(Integer,nullable=True)
    permanentLabAttendants = Column(Integer,nullable=True)
    temporaryLabAttendants = Column(Integer,nullable=True)
    partTimeLabAttendants = Column(Integer,nullable=True)
    permanentAccountant = Column(Integer,nullable=True)
    temporaryAccountant = Column(Integer,nullable=True)
    partTimeAccountant = Column(Integer,nullable=True)
    permanentPeonesClerk = Column(Integer,nullable=True)
    temporaryPeonesClerk = Column(Integer,nullable=True)
    partTimePeonesClerk = Column(Integer,nullable=True)
    permanentOthers = Column(Integer,nullable=True)
    temporaryOthers = Column(Integer,nullable=True)
    partTimeOthers = Column(Integer,nullable=True)
    