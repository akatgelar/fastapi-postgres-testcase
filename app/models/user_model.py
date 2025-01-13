from datetime import datetime
from zoneinfo import ZoneInfo
from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from app.config.database import Base

class UserModel(Base):
    __tablename__ = 'users' 
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    fullname: Mapped[str] = mapped_column(nullable=True)
    role: Mapped[str] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=False)
    created_by: Mapped[int] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(ZoneInfo('Asia/Jakarta')))
    updated_by: Mapped[int] = mapped_column(nullable=True)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(ZoneInfo('Asia/Jakarta')))

class UserSchema(BaseModel): 
    username: str
    password: str
    fullname: str
    role: str  
 