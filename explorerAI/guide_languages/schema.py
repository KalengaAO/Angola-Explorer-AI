from datetime import datetime

from pydantic import BaseModel


class GuideLanguageBase(BaseModel):
    guide_id: int
    language: str


class GuideLanguageCreate(GuideLanguageBase):
    pass


class GuideLanguageUpdate(BaseModel):
    language: str | None = None


class GuideLanguageResponse(GuideLanguageBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True