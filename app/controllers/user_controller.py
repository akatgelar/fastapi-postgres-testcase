#pylint: disable = no-self-argument, no-member
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.helpers.helper import Helper
from app.models.user_model import UserModel, UserSchema

class UserController(object):

    def get_all(db: Session):
        try:
            datas = db.query(UserModel).all()
            datas_final = []
            for data in datas: 
                del data.password
                datas_final.append(data)
            return datas_final
        except Exception as e:
            error_msg = f"Internal server error occurred: {str(e)}"
            raise HTTPException(status_code=500, detail=error_msg) from e
        
    def get_by_id(ids: int, db: Session):
        try:
            datas = db.query(UserModel).filter(UserModel.id == ids).first()
            del datas.password
            return datas
        except Exception as e:
            error_msg = f"Internal server error occurred: {str(e)}"  
            raise HTTPException(status_code=500, detail=error_msg) from e

    def create(data: UserSchema, db: Session):
        try:
            datas = UserModel(**data.model_dump())
            db.add(datas)
            db.commit()
            db.refresh(datas) 
            del datas.password
            return datas
        except Exception as e:
            error_msg = f"Internal server error occurred: {str(e)}"
            raise HTTPException(status_code=500, detail=error_msg) from e

    def update(data: UserSchema, ids: int, db: Session):
        try: 
            datas = db.get(UserModel, ids)
            if datas is None:
                raise HTTPException(status_code=400, detail='Data not found')

            for key, val in data.model_dump(exclude_none=True).items(): 
                if key == 'password': 
                    hashed_pass = Helper.hashed_password(val)
                    val = hashed_pass
                setattr(datas, key, val)

            db.commit()
            db.refresh(datas) 
            del datas.password
            return datas
        except Exception as e:
            error_msg = f"Internal server error occurred: {str(e)}"
            raise HTTPException(status_code=500, detail=error_msg) from e

    def delete(ids: int, db: Session):
        try: 
            datas = db.get(UserModel, ids)
            if datas is None:
                raise HTTPException(status_code=400, detail='Data not found')
 
            db.delete(datas)
            db.commit() 
            return datas
        except Exception as e:
            error_msg = f"Internal server error occurred: {str(e)}"
            raise HTTPException(status_code=500, detail=error_msg) from e
        
         