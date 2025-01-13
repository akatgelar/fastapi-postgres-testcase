from datetime import datetime
from zoneinfo import ZoneInfo
from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from app.config.database import Base

class ContentModel(Base):
    __tablename__ = 'contents' 
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    slug: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    content: Mapped[str] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=False)
    created_by: Mapped[int] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(ZoneInfo('Asia/Jakarta')))
    updated_by: Mapped[int] = mapped_column(nullable=True)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(ZoneInfo('Asia/Jakarta')))

class ContentSchema(BaseModel): 
    name: str
    title: str
    slug: str
    description: str
    content: str 
 