from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from explorerAI.database import Base


class Guide(Base):
    __tablename__ = "guides"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    city = Column(String(100), nullable=False)

    biography = Column(Text)

    experience_years = Column(Integer)

    photo = Column(String(255))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )