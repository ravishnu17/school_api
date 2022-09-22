from datetime import datetime, timedelta
from jose import JWTError , jwt
from Schema import schema
from Configuration import config
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends ,status , HTTPException

url = OAuth2PasswordBearer(tokenUrl="login")

secret_key = config.setting.secret_key
algorithm = config.setting.algorithm
expire = config.setting.token_expiration

def create_token(data : dict):
    encode = data.copy()
    expire_time = datetime.utcnow()+timedelta(minutes=expire)
    encode.update({"exp":expire_time})
    token = jwt.encode(encode , secret_key , algorithm=algorithm)
    return token

def verify(token : str , credential_exception):
    try:
        data = jwt.decode(token,secret_key , algorithms=algorithm)
        if data.get("id") is None :
            raise credential_exception
        token_data = schema.token(id = data.get("id") , role = data.get("role") , name = data.get("name"))
        return token_data
    except JWTError:
        raise credential_exception
    
def current_user(token : str = Depends(url)):
    credential_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Unauthorized user")
    return verify(token , credential_exception)
        