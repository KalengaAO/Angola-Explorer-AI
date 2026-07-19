### O papel de cada ficheiro
## base.py

Será a classe base.

class BaseAgent:
    def run(self, question: str):
        raise NotImplementedError

Todos os agentes vão herdar daqui.

## guide_agent.py

Especializado em guias.
Exemplos de perguntas:
Quem conhece o Namibe?
Quem fala inglês?
Quem é especialista em gastronomia?

## recommendation_agent.py

Especializado em recomendações.
Exemplos:
Quero fazer um safari.
Quero visitar praias.
Tenho dois dias em Benguela.

## rag_agent.py

É o orquestrador.
Recebe:
Pergunta

Decide:
Guide Agent?

Recommendation Agent?
Knowledge?

Depois junta tudo.

## prompts.py

Aqui ficam todos os prompts.

Por exemplo:
Você é um assistente turístico especializado em Angola...
Assim os prompts não ficam espalhados pelo código.

## tools.py

É o mais importante.
Aqui criamos funções que consultam o banco.
Por exemplo:
search_guides()
search_destinations()
search_reviews()
search_attractions()
Essas funções vão utilizar o knowledge/service.py.

                     USER

                       │

                 POST /chat

                       │

                  FastAPI Router

                       │

                  RAG AGENT

                       │

        ┌──────────────┼──────────────┐

        │              │              │

 Guide Agent    Recommendation     Knowledge

        │              │

        └──────────────┼──────────────┘

                  tools.py

                       │

               knowledge/service.py

                       │

                  SQLAlchemy

                       │

                    SQLite

Ou seja, em vez de criar novos CRUDs, vamos fazer o sistema responder perguntas como:

"Quero visitar o Namibe durante a época seca. Que atrações existem? Que guia fala inglês e tem boas avaliações?"

Para responder isso, o agente terá de:

Procurar o destino.
Obter as atrações relacionadas.
Encontrar guias associados.
Filtrar por idioma.
Considerar as avaliações.
Montar uma resposta coerente.