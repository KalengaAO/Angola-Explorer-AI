from datetime import datetime

from pydantic import BaseModel


class GuideSpecialtyBase(BaseModel):
    guide_id: int
    specialty: str


class GuideSpecialtyCreate(GuideSpecialtyBase):
    pass


class GuideSpecialtyUpdate(BaseModel):
    specialty: str | None = None


class GuideSpecialtyResponse(GuideSpecialtyBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True