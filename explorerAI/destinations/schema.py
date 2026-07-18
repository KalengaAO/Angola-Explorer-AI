from datetime import datetime

from pydantic import BaseModel


class DestinationBase(BaseModel):
    name: str
    province: str
    city: str
    description: str
    history: str | None = None
    category: str
    latitude: float | None = None
    longitude: float | None = None
    best_season: str | None = None
    photo: str | None = None


class DestinationCreate(DestinationBase):
    pass


class DestinationUpdate(BaseModel):
    name: str | None = None
    province: str | None = None
    city: str | None = None
    description: str | None = None
    history: str | None = None
    category: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    best_season: str | None = None
    photo: str | None = None


class DestinationResponse(DestinationBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True