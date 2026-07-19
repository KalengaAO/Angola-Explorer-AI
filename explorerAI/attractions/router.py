from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from explorerAI.database import get_db
from . import models, schema


router = APIRouter(
    prefix="/attractions",
    tags=["attractions"]
)


@router.post("/", response_model=schema.AttractionResponse)
def create_attraction(
    attraction: schema.AttractionCreate,
    db: Session = Depends(get_db)
):
    db_attraction = models.Attraction(
        **attraction.model_dump()
    )

    db.add(db_attraction)
    db.commit()
    db.refresh(db_attraction)

    return db_attraction


@router.get("/", response_model=list[schema.AttractionResponse])
def get_attractions(
    db: Session = Depends(get_db)
):
    return db.query(models.Attraction).all()


@router.get("/{attraction_id}", response_model=schema.AttractionResponse)
def get_attraction(
    attraction_id: int,
    db: Session = Depends(get_db)
):
    attraction = (
        db.query(models.Attraction)
        .filter(models.Attraction.id == attraction_id)
        .first()
    )

    if not attraction:
        raise HTTPException(
            status_code=404,
            detail="Attraction not found"
        )

    return attraction


@router.put("/{attraction_id}", response_model=schema.AttractionResponse)
def update_attraction(
    attraction_id: int,
    attraction: schema.AttractionUpdate,
    db: Session = Depends(get_db)
):
    db_attraction = (
        db.query(models.Attraction)
        .filter(models.Attraction.id == attraction_id)
        .first()
    )

    if not db_attraction:
        raise HTTPException(
            status_code=404,
            detail="Attraction not found"
        )

    update_data = attraction.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_attraction, key, value)

    db.commit()
    db.refresh(db_attraction)

    return db_attraction


@router.delete("/{attraction_id}")
def delete_attraction(
    attraction_id: int,
    db: Session = Depends(get_db)
):
    attraction = (
        db.query(models.Attraction)
        .filter(models.Attraction.id == attraction_id)
        .first()
    )

    if not attraction:
        raise HTTPException(
            status_code=404,
            detail="Attraction not found"
        )

    db.delete(attraction)
    db.commit()

    return {
        "message": "Attraction deleted successfully"
    }