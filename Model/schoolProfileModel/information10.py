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
    classRoom=Column(Integer,nullable=True)
    staffRoom=Column(Integer,nullable=True)
    physicalLab=Column(Integer,nullable=True)
    chemistryLab=Column(Integer,nullable=True)
    biologylab=Column(Integer,nullable=True)
    mathsLab=Column(Integer,nullable=True)
    scienceLab=Column(Integer,nullable=True)
    library=Column(Integer,nullable=True)
    auditorium=Column(Integer,nullable=True)
    counselor=Column(Integer,nullable=True)
    parlor=Column(Integer,nullable=True)
    prayer=Column(Integer,nullable=True)
    sick=Column(Integer,nullable=True)
    canteen=Column(Integer,nullable=True)
    security=Column(Integer,nullable=True)
    otherRoom=Column(Integer,nullable=True)
    staffToilets=Column(Integer,nullable=True)
    studToilet=Column(Integer,nullable=True)
    teacher=Column(String,nullable=True)
    