from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.init_db import get_db
from app.jwt import authenticate_user, create_access_token
from sqlalchemy.orm import Session
from app.schemas import Token
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

@router.post('/login', response_model=Token)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={'sub': user.username}, expires_delete=access_token_expire)
    return Token(access_token=access_token, token_type='bearer')