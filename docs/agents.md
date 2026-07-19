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