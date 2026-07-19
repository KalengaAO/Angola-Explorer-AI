from pydantic import BaseModel


class AgentRequest(BaseModel):
    question: str
    language: str | None = None


class AgentResponse(BaseModel):
    answer: str


class AgentContext(BaseModel):
    destinations: list = []
    guides: list = []
    attractions: list = []
    reviews: list = []
    knowledge: list = []


class ToolResult(BaseModel):
    source: str
    data: dict | list