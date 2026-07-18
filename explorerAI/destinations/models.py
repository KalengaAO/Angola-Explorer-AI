from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.sql import func

from explorerAI.database import Base


class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    province = Column(String(100), nullable=False)

    city = Column(String(100), nullable=False)

    description = Column(Text, nullable=False)

    history = Column(Text)

    category = Column(String(50), nullable=False)

    latitude = Column(Float)

    longitude = Column(Float)

    best_season = Column(String(100))

    photo = Column(String(255))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )