\# SciScreen.



\*Scientific literature screening, simplified.\*



Ferramenta de apoio à triagem inicial de artigos científicos por meio da análise semântica de resumos com modelos de linguagem.



\*\*Python 3.13\*\* · \*\*Gemini API\*\* · \*\*Em desenvolvimento\*\*



\---



\## 01 / Visão geral



A seleção de estudos é uma etapa fundamental das revisões da literatura. Entretanto, a presença de palavras-chave em um resumo não garante que o trabalho seja relevante para a pergunta de pesquisa.



O \*\*SciScreen\*\* foi concebido para auxiliar nessa etapa, comparando o conteúdo de um resumo científico com o objetivo e os critérios de elegibilidade definidos pelo pesquisador.



A ferramenta utiliza um modelo de linguagem (LLM) para produzir uma avaliação preliminar, acompanhada de justificativa e evidências textuais.



\*\*O SciScreen não substitui a avaliação crítica do pesquisador nem determina a inclusão definitiva de um estudo.\*\*



\## 02 / Funcionamento



O fluxo de análise utiliza três entradas:



| Entrada | Descrição |

|---|---|

| Objetivo | Pergunta ou finalidade da revisão |

| Critérios | Condições de inclusão e exclusão dos estudos |

| Resumo | Abstract do artigo a ser avaliado |



\*\*Fluxo de processamento\*\*



```text

Objetivo da revisão

&#x20;       +

Critérios de elegibilidade

&#x20;       +

Resumo científico

&#x20;       |

&#x20;       v

Construção do prompt

&#x20;       |

&#x20;       v

Modelo de linguagem

&#x20;       |

&#x20;       v

Classificação preliminar

&#x20;       +

Justificativa e evidências

&#x20;       +

Recomendação para avaliação humana

```



A análise é realizada individualmente para cada resumo fornecido no terminal.



\## 03 / Classificação



O SciScreen trabalha com três categorias de triagem:



| Classificação | Interpretação |

|---|---|

| Potencialmente relevante | O resumo apresenta elementos compatíveis com os critérios estabelecidos |

| Potencialmente irrelevante | O resumo apresenta elementos que indicam incompatibilidade com os critérios |

| Informações insuficientes | O resumo não contém informações suficientes para uma avaliação preliminar fundamentada |



Cada resultado deve apresentar uma justificativa, evidências identificadas no texto e uma recomendação de próximo passo.



As classificações representam \*\*recomendações preliminares\*\*, não decisões definitivas de elegibilidade.



\## 04 / Estrutura do projeto



```text

projeto-p0/

├── main.py

├── prompt\_sciscreen.py

├── llm\_service.py

├── test\_prompt.py

├── teste\_gemini.py

├── listar\_modelos.py

├── simulador.py

├── requirements.txt

├── .env.example

├── .gitignore

└── README.md

```



| Arquivo | Responsabilidade |

|---|---|

| `main.py` | Receber entradas e apresentar a análise |

| `prompt\_sciscreen.py` | Construir as instruções enviadas à LLM |

| `llm\_service.py` | Gerenciar a comunicação com a API |

| `test\_prompt.py` | Verificar a construção do prompt |

| `teste\_gemini.py` | Testar a comunicação com o modelo |

| `listar\_modelos.py` | Consultar modelos disponibilizados pela API |

| `simulador.py` | Demonstrar uma saída fictícia, sem chamada à API |



\## 05 / Instalação



\*\*Pré-requisito:\*\* Python 3.13.



Clone o repositório:



```bash

git clone https://github.com/lazevsil-png/projeto-p0.git

cd projeto-p0

```



Crie um ambiente virtual:



```bash

python -m venv .venv

```



No Windows, usando o Prompt de Comando:



```cmd

.venv\\Scripts\\activate

```



Instale as dependências:



```bash

python -m pip install -r requirements.txt

```



Crie um arquivo `.env` na raiz do projeto, utilizando `.env.example` como referência:



```dotenv

GEMINI\_API\_KEY=SUA\_CHAVE\_AQUI

```



Substitua o valor de exemplo por uma chave válida da API.



\*\*Segurança:\*\* o arquivo `.env` contém informações sensíveis e não deve ser publicado no repositório.



\## 06 / Execução



Com o ambiente virtual ativado e a configuração concluída, execute:



```bash

python main.py

```



O programa solicitará o objetivo da revisão, os critérios de elegibilidade e o resumo científico.



\*\*Estado atual:\*\* a entrada de dados e a construção do prompt foram implementadas. A integração com o Gemini ainda está em validação devido a respostas de indisponibilidade do serviço durante os testes.



\### Testes locais



Para verificar a construção do prompt:



```bash

python -m unittest test\_prompt.py

```



Para executar a demonstração fictícia:



```bash

python simulador.py

```



O simulador não realiza chamadas à API e não comprova o funcionamento da integração com a LLM.



\## 07 / Limitações



\- A classificação depende da qualidade das informações fornecidas e da resposta do modelo.

\- Resumos podem omitir informações necessárias para avaliar os critérios de elegibilidade.

\- Modelos de linguagem podem produzir interpretações incorretas ou justificativas sem suporte textual adequado.

\- A versão inicial processa um resumo por execução e não realiza buscas automáticas em bases bibliográficas.

\- A integração com a API ainda precisa ser validada por uma execução real bem-sucedida.



O resultado deve ser interpretado como apoio à triagem, mantendo a decisão final sob responsabilidade humana.



\## 08 / Desenvolvimento



O SciScreen está sendo desenvolvido no âmbito do \*\*P0 — Primeiro fluxo com LLM\*\*, da capacitação do Instituto Hardware BR.



O projeto busca demonstrar um fluxo reproduzível de desenvolvimento em Python, envolvendo integração com LLM, organização modular, proteção de credenciais, tratamento de falhas, testes e documentação.



A evolução será registrada por etapas, conforme os requisitos da capacitação.



\---



\*\*SciScreen.\*\*  

\*Research support, not automated scientific judgment.\*

