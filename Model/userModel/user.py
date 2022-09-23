from enum import unique
from sqlalchemy import Column, Integer,String ,Boolean , TIME ,Date,BigInteger,ForeignKey, ARRAY
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from DataBase.db import Base
from sqlalchemy.orm import relationship
    
class User(Base):
    __tablename__="user_data"
    
    id=Column(Integer,primary_key=True,nullable=False)
    name=Column(String,nullable=False)
    gender=Column(String,nullable=False)
    dob=Column(Date,nullable=False)
    mobile=Column(BigInteger,nullable=False)
    email=Column(String,nullable=False,unique=True)
    username=Column(String,nullable=False , unique=True)
    password=Column(String,nullable=False)
    role=Column(Integer,nullable=False )
    district=Column(String,nullable=False)
    time=Column(TIMESTAMP,nullable=False,server_default=text('now()'))