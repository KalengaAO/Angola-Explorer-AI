from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func

from explorerAI.database import Base


class GuideLanguage(Base):
    __tablename__ = "guide_languages"

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

    language = Column(
        String(50),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )