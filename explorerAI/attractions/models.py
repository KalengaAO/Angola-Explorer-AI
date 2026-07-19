from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from explorerAI.database import Base


class Attraction(Base):
    __tablename__ = "attractions"

    id = Column(Integer, primary_key=True, index=True)

    destination_id = Column(
        Integer,
        ForeignKey("destinations.id"),
        nullable=False
    )

    name = Column(String(100), nullable=False)

    description = Column(Text, nullable=False)

    history = Column(Text)

    category = Column(String(50))

    latitude = Column(Float)

    longitude = Column(Float)

    photo = Column(String(255))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )

    destination = relationship("Destination")