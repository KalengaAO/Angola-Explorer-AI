from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from explorerAI.database import get_db
from . import models, schema


router = APIRouter(
    prefix="/guide-languages",
    tags=["guide_languages"]
)


@router.post("/", response_model=schema.GuideLanguageResponse)
def create_guide_language(
    language: schema.GuideLanguageCreate,
    db: Session = Depends(get_db)
):
    db_language = models.GuideLanguage(
        **language.model_dump()
    )

    db.add(db_language)
    db.commit()
    db.refresh(db_language)

    return db_language


@router.get("/", response_model=list[schema.GuideLanguageResponse])
def get_guide_languages(
    db: Session = Depends(get_db)
):
    return db.query(models.GuideLanguage).all()


@router.get("/{language_id}", response_model=schema.GuideLanguageResponse)
def get_guide_language(
    language_id: int,
    db: Session = Depends(get_db)
):
    language = (
        db.query(models.GuideLanguage)
        .filter(models.GuideLanguage.id == language_id)
        .first()
    )

    if not language:
        raise HTTPException(
            status_code=404,
            detail="Guide language not found"
        )

    return language


@router.put("/{language_id}", response_model=schema.GuideLanguageResponse)
def update_guide_language(
    language_id: int,
    language: schema.GuideLanguageUpdate,
    db: Session = Depends(get_db)
):
    db_language = (
        db.query(models.GuideLanguage)
        .filter(models.GuideLanguage.id == language_id)
        .first()
    )

    if not db_language:
        raise HTTPException(
            status_code=404,
            detail="Guide language not found"
        )

    update_data = language.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_language, key, value)

    db.commit()
    db.refresh(db_language)

    return db_language


@router.delete("/{language_id}")
def delete_guide_language(
    language_id: int,
    db: Session = Depends(get_db)
):
    language = (
        db.query(models.GuideLanguage)
        .filter(models.GuideLanguage.id == language_id)
        .first()
    )

    if not language:
        raise HTTPException(
            status_code=404,
            detail="Guide language not found"
        )

    db.delete(language)
    db.commit()

    return {
        "message": "Guide language deleted successfully"
    }