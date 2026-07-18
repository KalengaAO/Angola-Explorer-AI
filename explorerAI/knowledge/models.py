from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)
from sqlalchemy.sql import func

from explorerAI.database import Base


class Knowledge(Base):
    __tablename__ = "knowledge"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(150),
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    source_type = Column(
        String(50),
        nullable=False
    )

    source_id = Column(
        Integer,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )