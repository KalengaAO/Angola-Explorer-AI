from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from explorerAI.database import get_db
from . import models, schema


router = APIRouter(
    prefix="/guides",
    tags=["guides"]
)

@router.post("/", response_model=schema.GuideResponse)
def create_guide(
    guide: schema.GuideCreate,
    db: Session = Depends(get_db)
):

    db_guide = models.Guide(**guide.model_dump())

    db.add(db_guide)
    db.commit()
    db.refresh(db_guide)

    return db_guide

@router.get("/", response_model=list[schema.GuideResponse])
def get_guides(
    db: Session = Depends(get_db)
):

    guides = db.query(models.Guide).all()

    return guides

@router.get("/{guide_id}", response_model=schema.GuideResponse)
def get_guide(
    guide_id: int,
    db: Session = Depends(get_db)
):

    guide = db.query(models.Guide).filter(
        models.Guide.id == guide_id
    ).first()

    if not guide:
        raise HTTPException(
            status_code=404,
            detail="Guide not found"
        )

    return guide