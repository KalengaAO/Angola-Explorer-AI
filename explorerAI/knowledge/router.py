from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from explorerAI.database import get_db
from . import models, schema


router = APIRouter(
    prefix="/knowledge",
    tags=["knowledge"]
)


@router.post("/", response_model=schema.KnowledgeResponse)
def create_knowledge(
    knowledge: schema.KnowledgeCreate,
    db: Session = Depends(get_db)
):
    db_knowledge = models.Knowledge(
        **knowledge.model_dump()
    )

    db.add(db_knowledge)
    db.commit()
    db.refresh(db_knowledge)

    return db_knowledge


@router.get("/", response_model=list[schema.KnowledgeResponse])
def get_knowledge(
    db: Session = Depends(get_db)
):
    return db.query(models.Knowledge).all()


@router.get("/{knowledge_id}", response_model=schema.KnowledgeResponse)
def get_knowledge_by_id(
    knowledge_id: int,
    db: Session = Depends(get_db)
):
    knowledge = (
        db.query(models.Knowledge)
        .filter(models.Knowledge.id == knowledge_id)
        .first()
    )

    if not knowledge:
        raise HTTPException(
            status_code=404,
            detail="Knowledge not found"
        )

    return knowledge


@router.put("/{knowledge_id}", response_model=schema.KnowledgeResponse)
def update_knowledge(
    knowledge_id: int,
    knowledge: schema.KnowledgeUpdate,
    db: Session = Depends(get_db)
):
    db_knowledge = (
        db.query(models.Knowledge)
        .filter(models.Knowledge.id == knowledge_id)
        .first()
    )

    if not db_knowledge:
        raise HTTPException(
            status_code=404,
            detail="Knowledge not found"
        )

    update_data = knowledge.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_knowledge, key, value)

    db.commit()
    db.refresh(db_knowledge)

    return db_knowledge


@router.delete("/{knowledge_id}")
def delete_knowledge(
    knowledge_id: int,
    db: Session = Depends(get_db)
):
    knowledge = (
        db.query(models.Knowledge)
        .filter(models.Knowledge.id == knowledge_id)
        .first()
    )

    if not knowledge:
        raise HTTPException(
            status_code=404,
            detail="Knowledge not found"
        )

    db.delete(knowledge)
    db.commit()

    return {
        "message": "Knowledge deleted successfully"
    }