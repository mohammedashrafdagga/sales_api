from fastapi import APIRouter, Depends,HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.init_db import get_db
from app.jwt import authenticate_user, create_access_token, generate_hash_password
from sqlalchemy.orm import Session
from app.schemas import Token, User, UserCreateSuperuser
from datetime import timedelta
from app.settings import ACCESS_TOKEN_EXPIRE_MINUTES
'''
    - login, only for administer 
    - using JWT also for login
'''

# create router 
router= APIRouter(
    prefix='api/auth/',
    tags = ['authenticate']
)

# Login User
@router.post('/register', response_model=User)
async def register_user(from_data: UserCreateSuperuser, db:Session=Depends(get_db)):
    # check email and username and generate password
    if db.query(User).filter(User.username == from_data.username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='username your used is already exists, try again!!'
        )
    if db.query(User).filter(User.email == from_data.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='email your used is already exists, try again!!'
        )
    data = from_data.dict()
    password = data.pop('password')
    hash_password = generate_hash_password(password=password)
    new_user = UserCreateSuperuser(**data, password=hash_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post('/login', response_model=Token)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={'sub': user.username}, expires_delete=access_token_expire)
    return Token(access_token=access_token, token_type='bearer')