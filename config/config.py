from pydantic import BaseSettings

class Setting(BaseSettings):
    db_host:str
    db_port : str
    db_username : str
    db_password : str
    db_name:str
    secret_key :str
    algorithm:str
    token_expiration:int
    class Config:
        env_file='.env'
        
setting = Setting()        