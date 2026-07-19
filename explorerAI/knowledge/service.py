from sqlalchemy.orm import Session

from . import models as knowledge_models
from guides import models as guide_models
from destinations import models as destination_models
from attractions import models as attraction_models
from reviews import models as review_models
from guide_languages import models as guide_language_models
from guide_specialties import models as guide_specialty_models


def create_knowledge(db: Session, title: str, content: str, source_type: str, source_id: int):
    knowledge = knowledge_models.Knowledge(title=title, content=content, source_type=source_type, source_id=source_id)
    db.add(knowledge)
    db.commit()
    db.refresh(knowledge)
    return knowledge


def search_guides(db: Session, city: str | None = None):
    query = db.query(guide_models.Guide)
    if city:
        query = query.filter(guide_models.Guide.city.ilike(f"%{city}%"))
    return query.all()


def get_guide(db: Session, guide_id: int):
    return db.query(guide_models.Guide).filter(guide_models.Guide.id == guide_id).first()


def get_guide_languages(db: Session, guide_id: int):
    return db.query(guide_language_models.GuideLanguage).filter(guide_language_models.GuideLanguage.guide_id == guide_id).all()


def get_guide_specialties(db: Session, guide_id: int):
    return db.query(guide_specialty_models.GuideSpecialty).filter(guide_specialty_models.GuideSpecialty.guide_id == guide_id).all()


def get_guide_reviews(db: Session, guide_id: int):
    return db.query(review_models.Review).filter(review_models.Review.guide_id == guide_id).all()


def search_destinations(db: Session, name: str | None = None):
    query = db.query(destination_models.Destination)
    if name:
        query = query.filter(destination_models.Destination.name.ilike(f"%{name}%"))
    return query.all()


def get_destination(db: Session, destination_id: int):
    return db.query(destination_models.Destination).filter(destination_models.Destination.id == destination_id).first()


def get_attractions(db: Session, destination_id: int):
    return db.query(attraction_models.Attraction).filter(attraction_models.Attraction.destination_id == destination_id).all()


def get_best_reviews(db: Session, limit: int = 5):
    return db.query(review_models.Review).order_by(review_models.Review.rating.desc()).limit(limit).all()


def search_knowledge(db: Session, keyword: str):
    return db.query(knowledge_models.Knowledge).filter(knowledge_models.Knowledge.content.ilike(f"%{keyword}%")).all()
