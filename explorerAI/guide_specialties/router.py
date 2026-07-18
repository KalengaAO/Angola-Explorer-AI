from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from explorerAI.database import get_db
from . import models, schema


router = APIRouter(
    prefix="/guide-specialties",
    tags=["guide_specialties"]
)


@router.post("/", response_model=schema.GuideSpecialtyResponse)
def create_guide_specialty(
    specialty: schema.GuideSpecialtyCreate,
    db: Session = Depends(get_db)
):
    db_specialty = models.GuideSpecialty(
        **specialty.model_dump()
    )

    db.add(db_specialty)
    db.commit()
    db.refresh(db_specialty)

    return db_specialty


@router.get("/", response_model=list[schema.GuideSpecialtyResponse])
def get_guide_specialties(
    db: Session = Depends(get_db)
):
    return db.query(models.GuideSpecialty).all()


@router.get("/{specialty_id}", response_model=schema.GuideSpecialtyResponse)
def get_guide_specialty(
    specialty_id: int,
    db: Session = Depends(get_db)
):
    specialty = (
        db.query(models.GuideSpecialty)
        .filter(models.GuideSpecialty.id == specialty_id)
        .first()
    )

    if not specialty:
        raise HTTPException(
            status_code=404,
            detail="Guide specialty not found"
        )

    return specialty


@router.put("/{specialty_id}", response_model=schema.GuideSpecialtyResponse)
def update_guide_specialty(
    specialty_id: int,
    specialty: schema.GuideSpecialtyUpdate,
    db: Session = Depends(get_db)
):
    db_specialty = (
        db.query(models.GuideSpecialty)
        .filter(models.GuideSpecialty.id == specialty_id)
        .first()
    )

    if not db_specialty:
        raise HTTPException(
            status_code=404,
            detail="Guide specialty not found"
        )

    update_data = specialty.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_specialty, key, value)

    db.commit()
    db.refresh(db_specialty)

    return db_specialty


@router.delete("/{specialty_id}")
def delete_guide_specialty(
    specialty_id: int,
    db: Session = Depends(get_db)
):
    specialty = (
        db.query(models.GuideSpecialty)
        .filter(models.GuideSpecialty.id == specialty_id)
        .first()
    )

    if not specialty:
        raise HTTPException(
            status_code=404,
            detail="Guide specialty not found"
        )

    db.delete(specialty)
    db.commit()

    return {
        "message": "Guide specialty deleted successfully"
    }