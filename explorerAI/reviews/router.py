from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from explorerAI.database import get_db
from . import models, schema


router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)


@router.post("/", response_model=schema.ReviewResponse)
def create_review(
    review: schema.ReviewCreate,
    db: Session = Depends(get_db)
):
    db_review = models.Review(
        **review.model_dump()
    )

    db.add(db_review)
    db.commit()
    db.refresh(db_review)

    return db_review


@router.get("/", response_model=list[schema.ReviewResponse])
def get_reviews(
    db: Session = Depends(get_db)
):
    return db.query(models.Review).all()


@router.get("/{review_id}", response_model=schema.ReviewResponse)
def get_review(
    review_id: int,
    db: Session = Depends(get_db)
):
    review = (
        db.query(models.Review)
        .filter(models.Review.id == review_id)
        .first()
    )

    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return review


@router.put("/{review_id}", response_model=schema.ReviewResponse)
def update_review(
    review_id: int,
    review: schema.ReviewUpdate,
    db: Session = Depends(get_db)
):
    db_review = (
        db.query(models.Review)
        .filter(models.Review.id == review_id)
        .first()
    )

    if not db_review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    update_data = review.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_review, key, value)

    db.commit()
    db.refresh(db_review)

    return db_review


@router.delete("/{review_id}")
def delete_review(
    review_id: int,
    db: Session = Depends(get_db)
):
    review = (
        db.query(models.Review)
        .filter(models.Review.id == review_id)
        .first()
    )

    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    db.delete(review)
    db.commit()

    return {
        "message": "Review deleted successfully"
    }