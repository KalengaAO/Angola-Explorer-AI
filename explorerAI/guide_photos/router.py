from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from explorerAI.database import get_db
from . import models, schema


router = APIRouter(
    prefix="/guide-photos",
    tags=["guide_photos"]
)


@router.post("/", response_model=schema.GuidePhotoResponse)
def create_guide_photo(
    photo: schema.GuidePhotoCreate,
    db: Session = Depends(get_db)
):
    db_photo = models.GuidePhoto(
        **photo.model_dump()
    )

    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)

    return db_photo


@router.get("/", response_model=list[schema.GuidePhotoResponse])
def get_guide_photos(
    db: Session = Depends(get_db)
):
    return db.query(models.GuidePhoto).all()


@router.get("/{photo_id}", response_model=schema.GuidePhotoResponse)
def get_guide_photo(
    photo_id: int,
    db: Session = Depends(get_db)
):
    photo = (
        db.query(models.GuidePhoto)
        .filter(models.GuidePhoto.id == photo_id)
        .first()
    )

    if not photo:
        raise HTTPException(
            status_code=404,
            detail="Guide photo not found"
        )

    return photo


@router.put("/{photo_id}", response_model=schema.GuidePhotoResponse)
def update_guide_photo(
    photo_id: int,
    photo: schema.GuidePhotoUpdate,
    db: Session = Depends(get_db)
):
    db_photo = (
        db.query(models.GuidePhoto)
        .filter(models.GuidePhoto.id == photo_id)
        .first()
    )

    if not db_photo:
        raise HTTPException(
            status_code=404,
            detail="Guide photo not found"
        )

    update_data = photo.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_photo, key, value)

    db.commit()
    db.refresh(db_photo)

    return db_photo


@router.delete("/{photo_id}")
def delete_guide_photo(
    photo_id: int,
    db: Session = Depends(get_db)
):
    photo = (
        db.query(models.GuidePhoto)
        .filter(models.GuidePhoto.id == photo_id)
        .first()
    )

    if not photo:
        raise HTTPException(
            status_code=404,
            detail="Guide photo not found"
        )

    db.delete(photo)
    db.commit()

    return {
        "message": "Guide photo deleted successfully"
    }