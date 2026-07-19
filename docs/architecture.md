# Roadmap do MVP *** AGENTE RAG ***

✅ Revisão rápida dos CRUDs (PUT/DELETE onde faltar). -1
✅ Criar a pasta agents/.
✅ Refatorar knowledge/service.py para ser o ponto central de acesso aos dados.
✅ Criar o primeiro agente (Guide Agent), capaz de responder perguntas usando os dados do banco.
✅ Integrar esse agente com um endpoint do FastAPI, por exemplo:

Mostrar capacidade de engenharia e IA.
Perder tempo com infraestrutura que não agrega valor ao avaliador.

## Sprint 1 --- Infraestrutura

## Role:

tourist
guide
admin

### Estrutura
## APP

Angola-exploer-AI/
│
├── users
│
├── guides
│
├── destinations
│
├── attractions
│
├── posts
│
├── reviews
│
├── publications 
│
├── guide_photos
│
├── guide_languages
│
├── guide_specialties
│
└── knowledge

## Frontedn
    app/
    components/
    pages/
    services/
    hooks/
    types/

                  Angola Explorer AI

                 ┌─────────────────┐
                 │    Tourist      │
                 │   Frontend      │
                 └────────┬────────┘
                          │
                          │ HTTP Request
                          ▼

                 ┌─────────────────┐
                 │    FastAPI      │
                 │     Router      │
                 └────────┬────────┘
                          │
                          │ Validate Request
                          │ Pydantic Schema
                          ▼

        ┌────────────────────────────────┐
        │          Business Layer        │
        │                                │
        │  guides                        │
        │  destinations                  │
        │  attractions                   │
        │  reviews                       │
        │  publications                  │
        │  guide_languages               │
        │  guide_specialties             │
        │  guide_photos                  │
        └───────────────┬────────────────┘
                        │
                        │ SQLAlchemy ORM
                        ▼

              ┌─────────────────┐
              │    SQLite DB    │
              │  exploreAI.db   │
              └────────┬────────┘
                       │
                       │ Extract Information
                       ▼

              ┌─────────────────┐
              │    Knowledge    │
              │     Layer       │
              └────────┬────────┘
                       │
                       │ Prepared Context
                       ▼

              ┌─────────────────┐
              │    AI Agent     │
              │      RAG        │
              └────────┬────────┘
                       │
                       │ Recommendation
                       ▼

              ┌─────────────────┐
              │     Tourist     │
              │    Response     │
              └─────────────────┘