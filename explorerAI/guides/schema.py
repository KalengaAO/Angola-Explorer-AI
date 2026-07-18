from pydantic import BaseModel
from datetime import datetime


class GuideBase(BaseModel):
    name: str
    email: str
    city: str
    biography: str | None = None
    experience_years: int | None = None
    photo: str | None = None


class GuideCreate(GuideBase):
    pass


class GuideResponse(GuideBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True