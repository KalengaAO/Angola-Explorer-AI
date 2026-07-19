from sqlalchemy.orm import Session

from knowledge import service


def search_guides(db: Session, city: str | None = None):
    return service.search_guides(db, city)


def get_guide(db: Session, guide_id: int):
    return service.get_guide(db, guide_id)


def get_guide_languages(db: Session, guide_id: int):
    return service.get_guide_languages(db, guide_id)


def get_guide_specialties(db: Session, guide_id: int):
    return service.get_guide_specialties(db, guide_id)


def get_guide_reviews(db: Session, guide_id: int):
    return service.get_guide_reviews(db, guide_id)


def search_destinations(db: Session, name: str | None = None):
    return service.search_destinations(db, name)


def get_destination(db: Session, destination_id: int):
    return service.get_destination(db, destination_id)


def get_attractions(db: Session, destination_id: int):
    return service.get_attractions(db, destination_id)


def get_best_reviews(db: Session, limit: int = 5):
    return service.get_best_reviews(db, limit)


def search_knowledge(db: Session, keyword: str):
    return service.search_knowledge(db, keyword)
