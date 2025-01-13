#pylint: disable = no-self-argument, no-member
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.content_model import ContentModel, ContentSchema

class ContentController(object):

    def get_all(db: Session):
        try:
            datas = db.query(ContentModel).all()
            datas = list(datas)
            return datas
        except Exception as e:
            error_msg = f"Internal server error occurred: {str(e)}"
            raise HTTPException(status_code=500, detail=error_msg) from e
        
    def get_by_id(ids: int, db: Session):
        try:
            datas = db.query(ContentModel).filter(ContentModel.id == ids).first()
            return datas
        except Exception as e:
            error_msg = f"Internal server error occurred: {str(e)}"  
            raise HTTPException(status_code=500, detail=error_msg) from e

    def create(data: ContentSchema, db: Session):
        try:
            datas = ContentModel(**data.model_dump())
            db.add(datas)
            db.commit()
            db.refresh(datas)
            return datas
        except Exception as e:
            error_msg = f"Internal server error occurred: {str(e)}"
            raise HTTPException(status_code=500, detail=error_msg) from e

    def update(data: ContentSchema, ids: int, db: Session):
        try: 
            datas = db.get(ContentModel, ids)
            if datas is None:
                raise HTTPException(status_code=400, detail='Data not found')

            for key, val in data.model_dump(exclude_none=True).items():
                setattr(datas, key, val)

            db.commit()
            db.refresh(datas) 
            return datas
        except Exception as e:
            error_msg = f"Internal server error occurred: {str(e)}"
            raise HTTPException(status_code=500, detail=error_msg) from e

    def delete(ids: int, db: Session):
        try: 
            datas = db.get(ContentModel, ids)
            if datas is None:
                raise HTTPException(status_code=400, detail='Data not found')
 
            db.delete(datas)
            db.commit() 
            return datas
        except Exception as e:
            error_msg = f"Internal server error occurred: {str(e)}"
            raise HTTPException(status_code=500, detail=error_msg) from e
        
         