from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.config import setting

SQLALCHEMY_DATABASE_URL=f'postgresql://{setting.db_username}:{setting.db_password}@{setting.db_host}/{setting.db_name}' #'://user:password@host/db_name'
try:
    engine=create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
    print("success")
except Exception as error :
    print("error")    

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()  
              