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
    middayScheme=Column(String,nullable=True)
    noOwnBus=Column(Integer,nullable=True)
    gpsCamera=Column(Integer,nullable=True)
    noladyAttend=Column(Integer,nullable=True)
    firstAid=Column(Integer,nullable=True)
    noDrinkWater=Column(Integer,nullable=True)
    BusContract=Column(Integer,nullable=True)
    buspass=Column(String,nullable=True)
    freeTransport=Column(String,nullable=True)
    