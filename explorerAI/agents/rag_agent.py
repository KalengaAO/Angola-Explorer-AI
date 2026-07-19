from sqlalchemy.orm import Session

from .base import BaseAgent
from .tools import (
    search_destinations,
    search_guides,
    search_knowledge,
)


class RAGAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="RAG Agent"
        )


    def run(
        self,
        question: str,
        db: Session
    ):

        context = {
            "destinations": [],
            "guides": [],
            "knowledge": []
        }


        question_lower = question.lower()


        if any(
            word in question_lower
            for word in [
                "destino",
                "visitar",
                "lugar",
                "conhecer"
            ]
        ):
            context["destinations"] = (
                search_destinations(db)
            )

        if any(
            word in question_lower
            for word in [
                "guia",
                "guias",
                "acompanhar"
            ]
        ):
            context["guides"] = (
                search_guides(db)
            )

        context["knowledge"] = (
            search_knowledge(
                db,
                question
            )
        )


        return context