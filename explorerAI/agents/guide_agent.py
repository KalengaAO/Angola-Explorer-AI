from sqlalchemy.orm import Session

from .base import BaseAgent
from .tools import get_guide_languages, get_guide_reviews, get_guide_specialties, search_guides


class GuideAgent(BaseAgent):
    """Finds guides from the application database without inventing details."""

    def __init__(self):
        super().__init__(name="Guide Agent")

    def run(self, question: str, db: Session) -> dict:
        question_lower = question.casefold()
        matches = []
        for guide in search_guides(db):
            languages = [item.language for item in get_guide_languages(db, guide.id)]
            specialties = [item.specialty for item in get_guide_specialties(db, guide.id)]
            reviews = get_guide_reviews(db, guide.id)
            average_rating = round(sum(review.rating for review in reviews) / len(reviews), 1) if reviews else None
            searchable = " ".join([guide.name, guide.city, guide.biography or "", *languages, *specialties]).casefold()
            score = sum(term in searchable for term in question_lower.split() if len(term) > 2)
            matches.append({"name": guide.name, "city": guide.city, "experience_years": guide.experience_years, "languages": languages, "specialties": specialties, "average_rating": average_rating, "score": score})

        matches.sort(key=lambda guide: (guide.get("score"), guide.get("average_rating") or 0), reverse=True)
        relevant = [guide for guide in matches if guide.get("score") > 0] or matches
        if not relevant:
            return {"answer": "Não encontrei guias registados para esta pesquisa.", "guides": []}

        lines = []
        comma = ", "
        semicolon = "; "
        for guide in relevant[:5]:
            details = ["cidade: {}".format(guide.get("city"))]
            if guide.get("languages"):
                details.append("idiomas: {}".format(comma.join(guide.get("languages"))))
            if guide.get("specialties"):
                details.append("especialidades: {}".format(comma.join(guide.get("specialties"))))
            if guide.get("experience_years") is not None:
                details.append("experiência: {} anos".format(guide.get("experience_years")))
            if guide.get("average_rating") is not None:
                details.append("avaliação média: {}/5".format(guide.get("average_rating")))
            lines.append("- {} ({})".format(guide.get("name"), semicolon.join(details)))

        return {"answer": "Guias encontrados:\n" + "\n".join(lines), "guides": relevant[:5]}
