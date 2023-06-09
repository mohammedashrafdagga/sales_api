from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from app.models import User
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.init_db import get_db
from jose import JWTError, jwt
from app.settings import SECRET_KEY, ALGORITHM
from app.schemas import TokenData


pwd_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/auth/login')

credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

# for verifying passwords and generating hash password 
def verify_password(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)

def generate_hash_password(password:str):
    return pwd_context.hash(password)

# Get User
def get_user(username:str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise credentials_exception
    return user
    
# authentication for user
def authenticate_user( username: str, password: str, db:Session = Depends(get_db)):
    user = get_user(username=username, db=db)
    if not verify_password(password, user.password):
        return False
    return user


# Now creating access token
def create_access_token(data: dict, expires_delete: timedelta | None = None):
    to_encode = data.copy()
    if expires_delete:
        expire = datetime.utcnow() + expires_delete
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# create an access token based in login data
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db:Session = Depends(get_db)):
   
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username, db=db)
    return user

# get user superuser
async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if not current_user.is_active and not current_user.is_superuser:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user