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
    governingTrust=Column(String,nullable=True)
    governingMember=Column(Integer,nullable=True)
    governingTenure=Column(Integer,nullable=True)
    educativeCommunity=Column(String,nullable=True)
    educativeCommunityMember=Column(Integer,nullable=True)
    educativeCommunityTenure=Column(Integer,nullable=True)
    pta=Column(String,nullable=True)
    ptaMember=Column(Integer,nullable=True)
    ptaTenure=Column(Integer,nullable=True)
    