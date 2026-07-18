from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    user_id: int
    title: str
    content: str
    photo: str | None = None


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    photo: str | None = None


class PostResponse(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True