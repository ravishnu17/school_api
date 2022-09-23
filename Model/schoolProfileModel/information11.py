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
    boundryWall=Column(String,nullable=True)
    boundryWallStatus=Column(String,nullable=True)
    cctv=Column(String,nullable=True)
    dataSave=Column(String,nullable=True)
    noCamera=Column(Integer,nullable=True)
    maleGuard=Column(String,nullable=True)
    noMaleGuard=Column(Integer,nullable=True)
    femaleGuard=Column(String,nullable=True)
    noFemaleGuard=Column(Integer,nullable=True)
    drinkWater=Column(String,nullable=True)
    drainage=Column(String,nullable=True)
    