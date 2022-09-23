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
    libraryOpenTime=Column(TIME,nullable=True)
    libraryCloseTime=Column(TIME,nullable=True)
    noBook=Column(Integer,nullable=True)
    noMagazine=Column(Integer,nullable=True)
    noNews=Column(Integer,nullable=True)
    noEbook=Column(Integer,nullable=True)
    primaryLibrary=Column(String,nullable=True)
    remedial=Column(String,nullable=True)
    tv=Column(Boolean,nullable=True)
    digitalboard=Column(Boolean,nullable=True)
    computer=Column(Boolean,nullable=True)
    projector=Column(Boolean,nullable=True)
    tape = Column(Boolean,nullable=True)
    