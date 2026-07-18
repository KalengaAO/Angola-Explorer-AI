# Roadmap do MVP *** AGENTE RAG ***

Definir a arquitetura e as entidades.
Configurar Docker + FastAPI + SQLlite.
Implementar autenticação (JWT com papéis admin, guide e user).
Desenvolver o CRUD de Guides.
Adicionar publicações, comentários, gostos e recomendações.
Construir um frontend simples para gerir e visualizar os guias.
Só então implementar os agentes, usando os dados que já existem.

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
        │  (Frontend)     │
        └────────┬────────┘
                 │
                 │
        ┌────────▼────────┐
        │    FastAPI      │
        │   Backend       │
        └────────┬────────┘
                 │
     ┌───────────┴───────────┐
     │                       │
┌────▼─────┐          ┌──────▼─────┐
│Knowledge │          │ AI Agent   │
│ Database │          │   RAG      │
└──────────┘          └────────────┘