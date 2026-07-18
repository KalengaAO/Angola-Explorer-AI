from datetime import datetime

from pydantic import BaseModel


class GuidePhotoBase(BaseModel):
    guide_id: int
    photo: str


class GuidePhotoCreate(GuidePhotoBase):
    pass


class GuidePhotoUpdate(BaseModel):
    photo: str | None = None


class GuidePhotoResponse(GuidePhotoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True