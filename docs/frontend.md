Criar projeto frontend (React/Vite ou Next.js)
Configurar cliente HTTP (axios ou fetch)
Criar layout principal
Integrar GET /destinations
Integrar GET /guides
Criar página de detalhe
Criar chat placeholder

Depois o Codex pode ajudar a acelerar componentes.

frontend/
│
├── src/
│   │
│   ├── api/
│   │   └── api.js              # comunicação com FastAPI
│   │
│   ├── components/
│   │   ├── Navbar.jsx
│   │   ├── DestinationCard.jsx
│   │   └── GuideCard.jsx
│   │
│   ├── pages/
│   │   ├── Home.jsx
│   │   ├── Destinations.jsx
│   │   ├── DestinationDetail.jsx
│   │   ├── Guides.jsx
│   │   └── Chat.jsx
│   │
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
├── package.json
└── vite.config.js