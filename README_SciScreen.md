# SciScreen.

*Scientific literature screening, simplified.*

Ferramenta de apoio à triagem inicial de artigos científicos por meio da análise semântica de resumos com modelos de linguagem.

Python 3.13 · Gemini API · **Em desenvolvimento**

---

## 01 / Visão geral

A presença de palavras-chave em um resumo não garante que um estudo seja relevante para uma pergunta de pesquisa. O **SciScreen** foi concebido para apoiar a triagem inicial de literatura científica, comparando o conteúdo de um resumo com o objetivo e os critérios de elegibilidade definidos pelo pesquisador.

A ferramenta propõe uma classificação preliminar acompanhada de justificativa, evidências textuais e recomendação para a próxima etapa de avaliação.

> O SciScreen não substitui a avaliação crítica do pesquisador nem determina a inclusão definitiva de um estudo.

## 02 / Funcionamento

O programa recebe três entradas:

| Entrada | Descrição |
| --- | --- |
| Objetivo | Pergunta ou finalidade da revisão |
| Critérios | Condições de inclusão e exclusão |
| Resumo | Texto do abstract a ser avaliado |

**Fluxo previsto**

```text
Objetivo + Critérios + Resumo
             |
             v
     Construção do prompt
             |
             v
     Modelo de linguagem
             |
             v
 Classificação + Justificativa
       + Evidências
       + Próximo passo
```

Na versão inicial, cada execução processa um resumo fornecido no terminal.

## 03 / Classificação

| Resultado | Interpretação |
| --- | --- |
| Potencialmente relevante | Há elementos compatíveis com os critérios definidos |
| Potencialmente irrelevante | Há elementos que indicam incompatibilidade com os critérios |
| Informações insuficientes | O resumo não permite uma avaliação preliminar fundamentada |

As categorias são **recomendações de triagem**, não decisões definitivas de elegibilidade.

## 04 / Estrutura

```text
projeto-p0/
├── main.py
├── prompt_sciscreen.py
├── llm_service.py
├── test_prompt.py
├── teste_gemini.py
├── listar_modelos.py
├── simulador.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | Receber entradas e apresentar o resultado |
| `prompt_sciscreen.py` | Construir as instruções para a LLM |
| `llm_service.py` | Realizar a comunicação com a API |
| `test_prompt.py` | Testar a construção do prompt |
| `teste_gemini.py` | Testar a comunicação com o Gemini |
| `listar_modelos.py` | Consultar modelos disponibilizados pela API |
| `simulador.py` | Exibir uma saída fictícia, sem chamada à API |

## 05 / Instalação

**Pré-requisito:** Python 3.13.

Clone o repositório:

```bash
git clone https://github.com/lazevsil-png/projeto-p0.git
cd projeto-p0
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative-o no **Prompt de Comando do Windows**:

```cmd
.venv\Scripts\activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto, seguindo o modelo `.env.example`:

```dotenv
GEMINI_API_KEY=SUA_CHAVE_AQUI
```

Substitua o valor de exemplo por sua chave válida. **Nunca publique o arquivo `.env` ou uma chave real.**

## 06 / Execução e testes

Com o ambiente configurado:

```bash
python main.py
```

O programa solicitará o objetivo da revisão, os critérios de elegibilidade e o resumo científico.

Para executar o teste local do prompt:

```bash
python -m unittest test_prompt.py
```

Para visualizar uma **demonstração fictícia**, sem acessar a API:

```bash
python simulador.py
```

**Estado atual:** a entrada de dados, a construção do prompt e um teste local foram implementados. A primeira chamada real bem-sucedida ao Gemini ainda está pendente; as tentativas realizadas retornaram erros de disponibilidade do serviço. O simulador não comprova a integração com a LLM.

## 07 / Limitações

- A qualidade da triagem depende das informações fornecidas e da resposta do modelo.
- Resumos podem omitir dados necessários para aplicar os critérios de elegibilidade.
- Modelos de linguagem podem gerar interpretações incorretas ou justificativas sem suporte textual.
- A versão inicial não busca artigos automaticamente nem processa lotes.
- A integração com a API ainda precisa ser validada por uma execução real bem-sucedida.

A decisão final de inclusão ou exclusão permanece sob responsabilidade do pesquisador.

## 08 / Desenvolvimento

Projeto desenvolvido no âmbito do **P0 — Primeiro fluxo com LLM**, da capacitação do **Instituto Hardware BR**.

O objetivo é construir um fluxo reproduzível em Python, com integração a um modelo de linguagem, proteção de credenciais, tratamento de falhas, testes e documentação. A evolução do projeto será registrada conforme os requisitos da capacitação.

---

**SciScreen.**  
*Research support, not automated scientific judgment.*
