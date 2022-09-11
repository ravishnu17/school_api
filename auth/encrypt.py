from passlib.context import CryptContext

pwd=CryptContext(schemes=['bcrypt'],deprecated='auto')

def hash(password):
    return pwd.hash(password)
def check(plainPassword,password):
    return pwd.verify(plainPassword,password)