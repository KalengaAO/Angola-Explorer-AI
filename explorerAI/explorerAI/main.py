from fastapi import FastAPI

from explorerAI.database import engine, Base
from guides.router import router as guide_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Angola Explorer AI",
    description="AI tourism platform for Angola",
    version="1.0.0"
)


app.include_router(guide_router)


@app.get("/")
def root():
    return {
        "message": "Angola Explorer AI API running"
    }