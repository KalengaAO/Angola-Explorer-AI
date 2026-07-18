from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from explorerAI.database import get_db
from . import models, schema


router = APIRouter(
    prefix="/destinations",
    tags=["destinations"]
)


@router.post("/", response_model=schema.DestinationResponse)
def create_destination(
    destination: schema.DestinationCreate,
    db: Session = Depends(get_db)
):
    db_destination = models.Destination(**destination.model_dump())

    db.add(db_destination)
    db.commit()
    db.refresh(db_destination)

    return db_destination


@router.get("/", response_model=list[schema.DestinationResponse])
def get_destinations(
    db: Session = Depends(get_db)
):
    return db.query(models.Destination).all()


@router.get("/{destination_id}", response_model=schema.DestinationResponse)
def get_destination(
    destination_id: int,
    db: Session = Depends(get_db)
):
    destination = (
        db.query(models.Destination)
        .filter(models.Destination.id == destination_id)
        .first()
    )

    if not destination:
        raise HTTPException(
            status_code=404,
            detail="Destination not found"
        )

    return destination


@router.put("/{destination_id}", response_model=schema.DestinationResponse)
def update_destination(
    destination_id: int,
    destination: schema.DestinationUpdate,
    db: Session = Depends(get_db)
):
    db_destination = (
        db.query(models.Destination)
        .filter(models.Destination.id == destination_id)
        .first()
    )

    if not db_destination:
        raise HTTPException(
            status_code=404,
            detail="Destination not found"
        )

    update_data = destination.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_destination, key, value)

    db.commit()
    db.refresh(db_destination)

    return db_destination


@router.delete("/{destination_id}")
def delete_destination(
    destination_id: int,
    db: Session = Depends(get_db)
):
    destination = (
        db.query(models.Destination)
        .filter(models.Destination.id == destination_id)
        .first()
    )

    if not destination:
        raise HTTPException(
            status_code=404,
            detail="Destination not found"
        )

    db.delete(destination)
    db.commit()

    return {
        "message": "Destination deleted successfully"
    }