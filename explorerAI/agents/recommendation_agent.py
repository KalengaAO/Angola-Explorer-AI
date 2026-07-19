from sqlalchemy.orm import Session

from .base import BaseAgent
from .tools import get_attractions, search_destinations


class RecommendationAgent(BaseAgent):
    """Recommends registered destinations and attractions for a travel request."""

    def __init__(self):
        super().__init__(name="Recommendation Agent")

    def run(self, question: str, db: Session) -> dict:
        question_lower = question.casefold()
        recommendations = []
        for destination in search_destinations(db):
            attractions = get_attractions(db, destination.id)
            attraction_text = " ".join("{} {} {}".format(item.name, item.category or "", item.description) for item in attractions)
            searchable = " ".join([destination.name, destination.province, destination.city, destination.category, destination.description, destination.best_season or "", attraction_text]).casefold()
            score = sum(term in searchable for term in question_lower.split() if len(term) > 2)
            recommendations.append({"destination": destination.name, "province": destination.province, "city": destination.city, "category": destination.category, "best_season": destination.best_season, "attractions": [item.name for item in attractions], "score": score})

        recommendations.sort(key=lambda item: item.get("score"), reverse=True)
        relevant = [item for item in recommendations if item.get("score") > 0] or recommendations
        if not relevant:
            return {"answer": "Não encontrei destinos ou atrações registados para esta recomendação.", "recommendations": []}

        lines = []
        comma = ", "
        semicolon = "; "
        for item in relevant[:3]:
            details = ["{}, {}".format(item.get("city"), item.get("province")), "categoria: {}".format(item.get("category"))]
            if item.get("best_season"):
                details.append("melhor época: {}".format(item.get("best_season")))
            if item.get("attractions"):
                details.append("atrações: {}".format(comma.join(item.get("attractions")[:5])))
            lines.append("- {} ({})".format(item.get("destination"), semicolon.join(details)))

        return {"answer": "Recomendações baseadas nos destinos registados:\n" + "\n".join(lines), "recommendations": relevant[:3]}
