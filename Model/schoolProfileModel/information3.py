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
    recognizedByGovern=Column(String,nullable=True)
    boardName=Column(String,nullable=True)
    affiliationNumber=Column(String,nullable=True)
    affiliationYear=Column(Integer,nullable=True)
    affiliationType=Column(String,nullable=True)
    affiliationStatement=Column(String,nullable=True)
    christian=Column(Integer,nullable=True)
    hindu=Column(Integer,nullable=True)
    islam=Column(Integer,nullable=True)
    others=Column(Integer,nullable=True)
    nonBeliver=Column(Integer,nullable=True)
    fire=Column(String,nullable=True)
    sanitation=Column(String,nullable=True)
    building=Column(String,nullable=True)
    minority=Column(String,nullable=True)
   