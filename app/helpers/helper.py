#pylint: disable = no-self-argument 
from passlib.context import CryptContext 
import time
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from app.config.config import config
from zoneinfo import ZoneInfo
from fastapi.encoders import jsonable_encoder

class Helper:
 
    def generate_response(action, data, status_code, is_success, pagination=None):
        messages = {
            "login": {
                "success": "Login successful", 
                "failure": "Login failed"
            },
            "get": {
                "success": "Get data successful", 
                "failure": "Get data failed"
            },
            "create": {
                "success": "Create data successful",
                "failure": "Create data failed",
            },
            "update": {
                "success": "Update data successful",
                "failure": "Update data failed",
            },
            "delete": {
                "success": "Delete data successful",
                "failure": "Delete data failed",
            },
        }

        success_message = messages[action]["success"]
        failure_message = messages[action]["failure"]

        message = success_message if is_success else failure_message 
        if pagination is not None:
            return {
                "message": message,
                "status_code": status_code,
                "success": int(is_success),
                "data": data,
                "pagination": pagination,
            }
        else:
            return {
                "message": message,
                "status_code": status_code,
                "success": int(is_success),
                "data": data,
            }
            
    def hashed_password(password: str) -> str: 
        password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return password_context.hash(password)


    def verify_password(password: str, hashed_pass: str) -> bool: 
        password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return password_context.verify(password, hashed_pass)
    
    def create_access_token(data: Union[str, Any], expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.now(ZoneInfo('Asia/Jakarta')) + expires_delta
        else:
            expires_delta = datetime.now(ZoneInfo('Asia/Jakarta')) + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
 
        to_encode = {"exp": expires_delta, "data": jsonable_encoder(data)}
        encoded_jwt = jwt.encode(to_encode, config.JWT_SECRET_KEY, config.ALGORITHM)
        return encoded_jwt
 
    def decode_jwt_token(token: str) -> dict:
        try:
            decoded_token = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.ALGORITHM]) 
            return decoded_token if decoded_token["exp"] >= time.time() else None
        except:
            return {}
        