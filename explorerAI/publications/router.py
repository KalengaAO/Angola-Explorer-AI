from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from explorerAI.database import get_db
from . import models, schema


router = APIRouter(
    prefix="/publications",
    tags=["publications"]
)


@router.post("/", response_model=schema.PublicationResponse)
def create_publication(
    publication: schema.PublicationCreate,
    db: Session = Depends(get_db)
):
    db_publication = models.Publication(
        **publication.model_dump()
    )

    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)

    return db_publication


@router.get("/", response_model=list[schema.PublicationResponse])
def get_publications(
    db: Session = Depends(get_db)
):
    return db.query(models.Publication).all()


@router.get("/{publication_id}", response_model=schema.PublicationResponse)
def get_publication(
    publication_id: int,
    db: Session = Depends(get_db)
):
    publication = (
        db.query(models.Publication)
        .filter(models.Publication.id == publication_id)
        .first()
    )

    if not publication:
        raise HTTPException(
            status_code=404,
            detail="Publication not found"
        )

    return publication


@router.put("/{publication_id}", response_model=schema.PublicationResponse)
def update_publication(
    publication_id: int,
    publication: schema.PublicationUpdate,
    db: Session = Depends(get_db)
):
    db_publication = (
        db.query(models.Publication)
        .filter(models.Publication.id == publication_id)
        .first()
    )

    if not db_publication:
        raise HTTPException(
            status_code=404,
            detail="Publication not found"
        )

    update_data = publication.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_publication, key, value)

    db.commit()
    db.refresh(db_publication)

    return db_publication


@router.delete("/{publication_id}")
def delete_publication(
    publication_id: int,
    db: Session = Depends(get_db)
):
    publication = (
        db.query(models.Publication)
        .filter(models.Publication.id == publication_id)
        .first()
    )

    if not publication:
        raise HTTPException(
            status_code=404,
            detail="Publication not found"
        )

    db.delete(publication)
    db.commit()

    return {
        "message": "Publication deleted successfully"
    }