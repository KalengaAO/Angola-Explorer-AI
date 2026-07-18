from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func

from explorerAI.database import Base


class GuidePhoto(Base):
    __tablename__ = "guide_photos"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    guide_id = Column(
        Integer,
        ForeignKey("guides.id"),
        nullable=False
    )

    photo = Column(
        String(255),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )