from datetime import datetime

from pydantic import BaseModel


class PublicationBase(BaseModel):
    user_id: int
    title: str
    content: str
    category: str | None = None
    photo: str | None = None


class PublicationCreate(PublicationBase):
    pass


class PublicationUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    category: str | None = None
    photo: str | None = None


class PublicationResponse(PublicationBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True