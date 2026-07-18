from datetime import datetime

from pydantic import BaseModel


class KnowledgeBase(BaseModel):
    title: str
    content: str
    source_type: str
    source_id: int


class KnowledgeCreate(KnowledgeBase):
    pass


class KnowledgeUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class KnowledgeResponse(KnowledgeBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True