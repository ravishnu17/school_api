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
    studentCouncil=Column(String,nullable=True)
    studentMember=Column(Integer,nullable=True)
    studentTenure=Column(Integer,nullable=True)
    generalComplaint=Column(String,nullable=True)
    schoolCommit=Column(String,nullable=True)
    constitutionCommit=Column(String,nullable=True)
    constitutionMember=Column(Integer,nullable=True)
    constitutionTenure=Column(Integer,nullable=True)
    