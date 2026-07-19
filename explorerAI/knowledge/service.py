from sqlalchemy.orm import Session

from . import models


def create_knowledge(
    db: Session,
    title: str,
    content: str,
    source_type: str,
    source_id: int
):
    knowledge = models.Knowledge(
        title=title,
        content=content,
        source_type=source_type,
        source_id=source_id
    )

    db.add(knowledge)
    db.commit()
    db.refresh(knowledge)

    return knowledge