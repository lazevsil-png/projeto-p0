# SciScreen.

*Scientific literature screening, simplified.*

Ferramenta de apoio à triagem inicial de artigos científicos por meio da análise semântica de resumos com modelos de linguagem.

Python 3.13 · GroqCloud API · **Em desenvolvimento**

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
├── test_llm_service.py
├── teste_groq.py
├── teste_gemini.py
├── listar_modelos.py
├── simulador.py
├── requirements.txt
├── .env.example
├── .gitignore
├── RELATORIO_EXECUCAO.md
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
| `test_llm_service.py` | Testar o serviço de LLM com respostas e falhas simuladas |
| `teste_groq.py` | Verificar a comunicação real com o GroqCloud |
| `RELATORIO_EXECUCAO.md` | Documentar a evolução, os testes e as decisões técnicas |


## 05 / Instalação

**Pré-requisito:** Python 3.13 e acesso à internet para comunicação com a API.

### Clonar o repositório

```bash
git clone https://github.com/lazevsil-png/projeto-p0.git
cd projeto-p0
```

### Criar o ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual no **Prompt de Comando do Windows (CMD)**:

```cmd
.venv\Scripts\activate
```

### Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
python -m pip install -r requirements.txt
```

As dependências principais do projeto são:

- `groq`: comunicação com a API do GroqCloud;
- `python-dotenv`: carregamento das variáveis de ambiente;
- `google-genai`: biblioteca mantida para os testes experimentais anteriores com Gemini.

### Configurar a chave de API

O SciScreen utiliza o **GroqCloud** como provedor principal de LLM, com o modelo `openai/gpt-oss-20b`.

Para utilizar o serviço, é necessário obter uma chave de API no [GroqCloud Console](https://console.groq.com/keys).

Na raiz do projeto, crie um arquivo `.env` a partir do modelo `.env.example`.

No **CMD do Windows**, é possível criar a cópia com:

```cmd
copy .env.example .env
```

Abra o arquivo `.env` e substitua o valor de exemplo pela sua chave válida:

```dotenv
GROQ_API_KEY=SUA_CHAVE_GROQ_AQUI
```

A variável `GEMINI_API_KEY` é opcional e utilizada apenas nos testes experimentais anteriores com Gemini.

**Segurança:** nunca publique o arquivo `.env` ou suas credenciais reais. O arquivo está incluído no `.gitignore` para evitar seu versionamento.

A utilização da API está sujeita aos limites e às condições do plano disponibilizado pelo provedor.

### Verificar a instalação

Para confirmar que as dependências foram instaladas corretamente, execute:

```bash
python -m unittest test_llm_service.py -v
```

Esse comando executa quatro testes automatizados utilizando simulações, sem realizar chamadas reais à API.

Para executar a aplicação com uma análise real, consulte a seção **06 / Execução e testes**.



## 06 / Execução e testes

Com o ambiente configurado, execute:

```bash
python main.py
```

O programa solicitará três informações:

1. Objetivo da revisão de literatura;
2. Critérios de inclusão e exclusão;
3. Resumo científico (abstract).

Após validar as entradas, o SciScreen constrói um prompt e o envia à API do GroqCloud, utilizando o modelo `openai/gpt-oss-20b`.

A resposta é apresentada no terminal, com uma avaliação preliminar da relevância do estudo.

### Testes automatizados

Para executar os testes do serviço de LLM:

```bash
python -m unittest test_llm_service.py -v
```

Os quatro testes verificam:

- Ausência da chave de API;
- Credencial inválida (HTTP 401);
- Falha de comunicação;
- Retorno de uma resposta válida.

Os testes utilizam simulações e não realizam chamadas reais à API.

**Resultado observado:** quatro testes aprovados, sem falhas.

Para executar os testes da construção do prompt:

```bash
python -m unittest test_prompt.py
```

### Demonstração sem API

Para visualizar uma saída fictícia, execute:

```bash
python simulador.py
```

O simulador não consulta uma LLM e não deve ser confundido com uma análise real.

### Estado da integração

A integração com o GroqCloud foi executada com sucesso, incluindo uma chamada real à LLM e a apresentação da análise no terminal.

A aplicação também demonstrou validação de entradas obrigatórias e tratamento de falhas simuladas.

A precisão científica das classificações ainda não foi avaliada sistematicamente.


### Exemplo de utilização

O exemplo a seguir é ilustrativo e demonstra como fornecer as informações solicitadas pelo programa.

**Objetivo da revisão:**

Identificar estudos que utilizam técnicas analíticas para a caracterização de resíduos de disparo de arma de fogo (GSR).

**Critérios de inclusão e exclusão:**

Incluir estudos experimentais que caracterizem GSR por técnicas instrumentais. Excluir trabalhos sem análise de resíduos de disparo.

**Abstract:**

This study investigates gunshot residue particles collected from firearm discharge using scanning electron microscopy coupled with energy-dispersive X-ray spectroscopy (SEM-EDS). The elemental composition and morphology of the particles were evaluated.

**Exemplo ilustrativo de resposta:**

```text
Classificação: Potencialmente relevante

Justificativa:
O estudo apresenta caracterização instrumental de
resíduos de disparo, compatível com o objetivo da revisão.

Evidência textual:
"The elemental composition and morphology of the
particles were evaluated."

Próximo passo:
Consultar o texto completo para verificar os
procedimentos experimentais e os critérios de elegibilidade.
```

A resposta acima é ilustrativa e não representa uma saída registrada de uma execução real. Resultados produzidos pela LLM podem variar.

O SciScreen oferece apoio à triagem inicial; a decisão de elegibilidade permanece sob responsabilidade do pesquisador.

## 07 / Limitações

- A qualidade da triagem depende da clareza dos objetivos e critérios fornecidos pelo pesquisador.
- Resumos científicos podem omitir informações necessárias para avaliar a elegibilidade de um estudo.
- A LLM pode produzir interpretações incorretas, classificações inconsistentes ou justificativas sem suporte no texto.
- A aplicação processa um resumo por execução e não realiza buscas automáticas em bases científicas.
- A comunicação com o GroqCloud depende de conexão com a internet, credencial válida, disponibilidade do serviço e limites de utilização da API.
- Os testes automatizados verificam o comportamento do código em cenários específicos, mas não demonstram a precisão científica das classificações.
- A instalação e a execução em um ambiente limpo ainda precisam ser verificadas.

O SciScreen é uma ferramenta de apoio à triagem preliminar. A decisão final de inclusão ou exclusão de artigos permanece sob responsabilidade do pesquisador.


## 08 / Desenvolvimento

O SciScreen está sendo desenvolvido no âmbito do **P0 — Primeiro fluxo com LLM**, da capacitação do **Instituto Hardware BR**.

O projeto utiliza Python 3.13 e integra o modelo `openai/gpt-oss-20b` por meio da API do GroqCloud.

O desenvolvimento contempla entrada e validação de dados, construção de prompts, comunicação com a LLM, proteção de credenciais e testes automatizados.

A evolução do projeto, as decisões técnicas, os testes realizados e as limitações identificadas estão documentados no [Relatório de Execução](RELATORIO_EXECUCAO.md).

**Situação atual:** fluxo principal funcional e testes automatizados aprovados. A documentação, a verificação de reprodutibilidade e as demais entregas da capacitação continuam em andamento.

---

**SciScreen.**  
*Research support, not automated scientific judgment.*
