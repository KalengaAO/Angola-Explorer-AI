from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func

from explorerAI.database import Base


class Publication(Base):
    __tablename__ = "publications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    title = Column(
        String(150),
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    category = Column(
        String(50)
    )

    photo = Column(
        String(255)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )