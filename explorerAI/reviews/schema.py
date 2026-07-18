from datetime import datetime

from pydantic import BaseModel


class ReviewBase(BaseModel):
    user_id: int
    guide_id: int | None = None
    destination_id: int | None = None
    rating: int
    comment: str


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    rating: int | None = None
    comment: str | None = None


class ReviewResponse(ReviewBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True