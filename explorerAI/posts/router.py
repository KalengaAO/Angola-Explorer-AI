from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from explorerAI.database import get_db
from . import models, schema


router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)


@router.post("/", response_model=schema.PostResponse)
def create_post(
    post: schema.PostCreate,
    db: Session = Depends(get_db)
):
    db_post = models.Post(
        **post.model_dump()
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post


@router.get("/", response_model=list[schema.PostResponse])
def get_posts(
    db: Session = Depends(get_db)
):
    return db.query(models.Post).all()


@router.get("/{post_id}", response_model=schema.PostResponse)
def get_post(
    post_id: int,
    db: Session = Depends(get_db)
):
    post = (
        db.query(models.Post)
        .filter(models.Post.id == post_id)
        .first()
    )

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    return post


@router.put("/{post_id}", response_model=schema.PostResponse)
def update_post(
    post_id: int,
    post: schema.PostUpdate,
    db: Session = Depends(get_db)
):
    db_post = (
        db.query(models.Post)
        .filter(models.Post.id == post_id)
        .first()
    )

    if not db_post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    update_data = post.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_post, key, value)

    db.commit()
    db.refresh(db_post)

    return db_post


@router.delete("/{post_id}")
def delete_post(
    post_id: int,
    db: Session = Depends(get_db)
):
    post = (
        db.query(models.Post)
        .filter(models.Post.id == post_id)
        .first()
    )

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    db.delete(post)
    db.commit()

    return {
        "message": "Post deleted successfully"
    }