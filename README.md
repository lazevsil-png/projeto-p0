

\# SciScreen



Assistente de triagem semântica de artigos científicos com LLM.



\## Sobre o projeto



O SciScreen é uma aplicação Python desenvolvida

para apoiar a triagem inicial de artigos científicos

em revisões da literatura.



O programa analisa o conteúdo de um abstract

considerando o objetivo da revisão e os critérios

de inclusão e exclusão definidos pelo pesquisador.



\## Problema



Buscas em bases científicas podem retornar artigos

que contêm palavras-chave ou siglas relacionadas

à pesquisa, mas que não correspondem ao tema

investigado.



A leitura manual dos resumos para identificar

esses resultados pode demandar bastante tempo.



\## Solução proposta



Utilizar um modelo de linguagem (LLM) para

interpretar semanticamente o abstract e fornecer

uma recomendação preliminar de triagem.



\## Entradas



\- Objetivo da revisão.

\- Critérios de inclusão e exclusão.

\- Abstract do artigo.



\## Saídas esperadas



\- Classificação preliminar de relevância.

\- Justificativa.

\- Evidências extraídas do abstract.

\- Recomendação para o pesquisador.



\## Classificações



1\. Potencialmente relevante.

2\. Potencialmente irrelevante.

3\. Informações insuficientes.



\## Tecnologias



\- Python 3.13

\- Google Gemini API

\- python-dotenv

\- Git e GitHub



\## Estado atual



Em desenvolvimento.



A entrada de dados, a validação e a preparação

do prompt estão implementadas.



A integração com a API foi desenvolvida, mas

ainda não foi validada por uma resposta real

bem-sucedida devido a erros HTTP 503.



\## Limitações



O SciScreen não substitui a avaliação humana,

não determina a elegibilidade definitiva de

artigos e não realiza buscas automáticas

em bases científicas nesta versão.



\## Projeto acadêmico



Desenvolvido para o P0 - Primeiro Fluxo com LLM,

da capacitação Hardware BR.



