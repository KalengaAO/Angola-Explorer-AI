from fastapi import FastAPI

from explorerAI.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# carregar models
from users import models as user_models
from guides import models as guide_models
from destinations import models as destination_models
from attractions import models as attraction_models
from posts import models as post_models
from reviews import models as review_models
from publications import models as publication_models
from guide_photos import models as guide_photo_models
from guide_languages import models as guide_language_models
from guide_specialties import models as guide_specialty_models
from knowledge import models as knowledge_models


Base.metadata.create_all(bind=engine)


# importar routers
from users.router import router as user_router
from guides.router import router as guide_router
from destinations.router import router as destination_router
from attractions.router import router as attraction_router
from posts.router import router as post_router
from reviews.router import router as review_router
from publications.router import router as publication_router
from guide_photos.router import router as guide_photo_router
from guide_languages.router import router as guide_language_router
from guide_specialties.router import router as guide_specialty_router
from knowledge.router import router as knowledge_router


app = FastAPI(
    title="Angola Explorer AI",
    description="AI tourism platform for Angola",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(guide_router)
app.include_router(destination_router)
app.include_router(attraction_router)
app.include_router(post_router)
app.include_router(review_router)
app.include_router(publication_router)
app.include_router(guide_photo_router)
app.include_router(guide_language_router)
app.include_router(guide_specialty_router)
app.include_router(knowledge_router)


@app.get("/")
def root():
    return {
        "message": "Angola Explorer AI API running"
    }