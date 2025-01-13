#pylint: disable = no-self-argument, no-member
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.user_model import UserModel
from app.helpers.helper import Helper

class AuthController(object):

    def login(auth_data: OAuth2PasswordRequestForm, db: Session):
        try:
            datas = db.query(UserModel).filter(UserModel.username == auth_data.username).first()
            if not datas:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User tidak ditemukan")
            
            if not Helper.verify_password(auth_data.password, datas.password):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password salah")
            
            del datas.password
            access_token = Helper.create_access_token(data=datas, expires_delta=None)
            
            result = {"access token" : access_token, "token_type": "bearer"}
            return result
        except Exception as e:
            error_msg = f"Internal server error occurred: {str(e)}"
            raise HTTPException(status_code=500, detail=error_msg) from e
         