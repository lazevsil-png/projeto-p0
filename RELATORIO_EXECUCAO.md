# SciScreen — Relatório de Execução

## 1. Identificação do projeto

**Projeto:** SciScreen — Triagem Científica Assistida por LLM

**Capacitação:** Instituto Hardware BR — P0: Primeiro fluxo com LLM

**Linguagem:** Python 3.13

**Interface:** Terminal

**Provedor de LLM:** GroqCloud

**Modelo utilizado:** openai/gpt-oss-20b

**Repositório:** https://github.com/lazevsil-png/projeto-p0

## 2. Problema identificado

A seleção de artigos científicos para revisões de literatura exige a leitura de resumos e a comparação de seu conteúdo com objetivos e critérios previamente definidos.

Esse processo pode ser repetitivo e consumir tempo, especialmente quando envolve muitos artigos.

O SciScreen foi desenvolvido como uma ferramenta experimental para auxiliar na triagem preliminar de resumos científicos, sem substituir a avaliação crítica do pesquisador.

## 3. Solução proposta

O SciScreen é uma aplicação Python executada pelo terminal.

O usuário informa:

- O objetivo da revisão de literatura;
- Os critérios de inclusão e exclusão;
- O resumo científico (abstract) a ser analisado.

A aplicação organiza essas informações em um prompt estruturado e o envia a um modelo de linguagem por meio de uma API.

O modelo retorna uma análise textual que auxilia o pesquisador a avaliar a possível relevância do artigo.

A decisão final de inclusão ou exclusão permanece sob responsabilidade humana.

## 4. Evolução do desenvolvimento

### 4.1. Nível Básico — Primeiro fluxo com LLM

O desenvolvimento começou com a criação de uma aplicação Python capaz de receber entradas textuais pelo terminal.

Foram implementadas a leitura dos campos, a validação de entradas obrigatórias e a construção de um prompt para análise científica.

Inicialmente, foram realizados experimentos de integração com a API do Google Gemini. Durante os testes, ocorreram dificuldades de disponibilidade e acesso aos modelos.

Posteriormente, a integração foi realizada com o GroqCloud, utilizando o modelo openai/gpt-oss-20b.

A aplicação conseguiu enviar um prompt real à LLM e apresentar a resposta no terminal, demonstrando o funcionamento do fluxo principal.

As credenciais foram armazenadas em um arquivo `.env`, excluído do controle de versão por meio do `.gitignore`.

O arquivo `.env.example` foi atualizado para indicar as variáveis necessárias à configuração do projeto.

### 4.2. Testes e tratamento de falhas

Foram realizados testes manuais e automatizados para verificar o comportamento da aplicação.

**Testes manuais:**

- Execução do fluxo principal com uma chamada real à LLM;
- Validação de campos vazios.

**Testes automatizados:**

Foi criado o arquivo `test_llm_service.py`, utilizando a biblioteca `unittest` e simulações com `unittest.mock`.

Foram verificados quatro cenários:

1. Ausência da chave de API;
2. Erro de autenticação HTTP 401;
3. Falha de comunicação;
4. Retorno de uma resposta válida da LLM.

Na primeira execução no ambiente de desenvolvimento, os quatro testes foram aprovados.

**Resultado observado:**

```text
Ran 4 tests in 0.004s
OK
```

Os testes foram implementados utilizando simulações do cliente Groq, sem realizar chamadas reais à API.

Entretanto, a verificação posterior em ambiente limpo revelou uma dependência não intencional da configuração local das credenciais, conforme descrito na seção seguinte.

### 4.3. Verificação de reprodutibilidade em ambiente limpo

Para verificar a possibilidade de reprodução do projeto por outros desenvolvedores, foi criada uma cópia independente do repositório público do SciScreen.

O procedimento foi realizado em ambiente Windows, utilizando Python 3.13, sem reutilizar o ambiente virtual do projeto original.

As seguintes etapas foram executadas:

1. Clonagem do repositório público do GitHub;
2. Criação de um novo ambiente virtual Python;
3. Ativação do ambiente virtual;
4. Instalação das dependências declaradas no arquivo `requirements.txt`;
5. Execução dos testes automatizados sem configurar uma chave de API real.

A instalação das dependências foi concluída com sucesso.

**Primeira execução dos testes em ambiente limpo**

Apesar da aprovação anterior dos testes no ambiente de desenvolvimento, a primeira execução na instalação independente apresentou três falhas.

```text
Ran 4 tests in 0.008s
FAILED (failures=3)
```

| Cenário avaliado | Resultado inicial |
|---|---|
| Chave de API ausente | Aprovado |
| Credencial inválida | Reprovado |
| Falha de comunicação | Reprovado |
| Resposta válida simulada | Reprovado |

Os três testes reprovados retornaram a mensagem de ausência da chave de API, em vez dos resultados esperados para cada cenário.

**Diagnóstico**

A análise do código revelou que os testes simulavam o cliente Groq, mas não simulavam a presença da variável de ambiente correspondente à chave de API.

Consequentemente, a aplicação interrompia a execução antes de alcançar os comportamentos simulados.

Esse resultado demonstrou que a aprovação inicial dos testes estava condicionada à configuração do ambiente de desenvolvimento.

**Correção implementada**

Foi adicionada uma simulação da leitura da variável de ambiente nos testes de credencial inválida, falha de comunicação e resposta válida:

```python
@patch("llm_service.os.getenv", return_value="chave_ficticia")
```

A alteração permitiu que os testes alcançassem os cenários simulados sem depender de credenciais reais.

O teste de ausência da chave foi preservado, assim como a estrutura do código principal da aplicação.

**Resultados após a correção**

Os testes foram executados novamente no ambiente original e na instalação independente.

| Ambiente de execução | Testes aprovados | Tempo |
|---|---:|---:|
| Ambiente original após correção | 4/4 | 0,007 s |
| Ambiente limpo após correção | 4/4 | 0,005 s |
| Ambiente limpo com código atualizado diretamente do GitHub | 4/4 | 0,005 s |

A correção foi registrada e publicada no repositório por meio do commit `b350cb2`, identificado pela mensagem:

```text
fix: torna testes independentes da chave de API
```

Após a publicação, a cópia de teste foi restaurada para eliminar a alteração manual e atualizada diretamente pelo GitHub.

A execução dos testes com a versão publicada apresentou o seguinte resultado:

```text
Ran 4 tests in 0.005s
OK
```

**Conclusão da verificação**

Os resultados demonstraram que as dependências declaradas puderam ser instaladas em um ambiente virtual independente e que os quatro testes automatizados do serviço de LLM puderam ser reproduzidos sem credenciais reais.

O procedimento também permitiu identificar e corrigir uma dependência não intencional da configuração local, evidenciando a importância dos testes em ambientes independentes.

A verificação foi limitada ao ambiente Windows utilizado e aos quatro testes do serviço de LLM, não constituindo uma validação integral da aplicação em diferentes sistemas operacionais.

### 4.4. Verificação complementar dos testes automatizados

Após a validação do serviço de LLM, foi executado o teste de construção do prompt científico no ambiente virtual independente.

Em seguida, os cinco testes automatizados foram executados conjuntamente:

```bash
python -m unittest test_prompt test_llm_service -v
```

**Resultado:** cinco testes aprovados, sem falhas.

### 4.5. Verificação de segurança das credenciais

Foram realizadas verificações direcionadas para identificar possíveis exposições acidentais de credenciais no repositório.

| Verificação | Resultado |
| --- | --- |
| Presença do arquivo .env no histórico local | Não identificada |
| Padrões de chaves GroqCloud no histórico | Não identificados |
| Padrões de chaves Gemini no histórico | Não identificados |
| Regra de exclusão no .gitignore | Confirmada |
| Rastreamento atual do arquivo .env pelo Git | Não identificado |

As verificações foram realizadas sem exibir ou compartilhar credenciais reais.

Os resultados não indicaram exposição de credenciais nos cenários investigados. Entretanto, essa inspeção foi direcionada aos padrões pesquisados e ao histórico disponível localmente, não constituindo uma auditoria exaustiva de segurança.

## 5. Decisões técnicas

A aplicação utiliza Python por sua simplicidade e disponibilidade de bibliotecas para integração com serviços de LLM.

A interface por terminal foi escolhida para manter o escopo compatível com o objetivo do P0, sem acrescentar complexidade de interface gráfica.

A separação entre construção do prompt, integração com a API e execução principal facilita a manutenção e os testes.

O uso de variáveis de ambiente evita inserir credenciais diretamente no código-fonte.

Os testes com simulações permitem verificar situações de falha sem depender da disponibilidade do serviço externo.

A simulação explícita da leitura das credenciais foi adotada para garantir a independência dos testes em relação às configurações locais.

A criação de um ambiente virtual separado permitiu verificar a instalação e a execução dos testes sem comprometer o ambiente original de desenvolvimento.

O controle de versão com Git e GitHub permitiu registrar a evolução do projeto, identificar a versão corrigida e verificar o comportamento do código efetivamente publicado.

## 6. Limitações identificadas

O SciScreen não realiza uma avaliação científica definitiva dos artigos.

As respostas da LLM podem apresentar erros de interpretação, omissões ou classificações inadequadas.

A qualidade da análise depende da clareza dos critérios fornecidos pelo usuário e do conteúdo do resumo.

O funcionamento com chamadas reais depende da disponibilidade do provedor, da validade da credencial e dos limites de utilização da API.

Os testes automatizados verificam comportamentos específicos do código, mas não validam a precisão científica das classificações.

A verificação de reprodutibilidade foi realizada em ambiente Windows com Python 3.13, não tendo sido estendida a outros sistemas operacionais.

Embora as versões das dependências diretas estejam especificadas no arquivo `requirements.txt`, as dependências transitivas não estão integralmente fixadas, podendo ocorrer variações em instalações futuras.

## 7. Próximas etapas

### 7.1. Atividades concluídas

- Implementação do fluxo principal de interação com a LLM;
- Integração com a API GroqCloud;
- Execução de uma chamada real à LLM;
- Implementação de testes automatizados para o serviço de LLM;
- Configuração da proteção local das credenciais;
- Publicação do código-fonte e da documentação inicial no GitHub;
- Documentação de um exemplo ilustrativo de entrada e saída no README;
- Instalação das dependências em ambiente virtual independente;
- Identificação e correção das falhas de reprodutibilidade dos testes;
- Verificação dos quatro testes do serviço de LLM utilizando a versão corrigida publicada no GitHub;
- Atualização do README com os resultados da verificação em ambiente limpo;
- Execução conjunta dos cinco testes automatizados em ambiente independente;
- Verificação direcionada do histórico e da proteção das credenciais.

### 7.2. Atividades pendentes

- Atualizar o README com os cinco testes aprovados e as verificações de segurança;
- Consolidar as evidências de execução da aplicação;
- Organizar as evidências dos níveis da capacitação;
- Verificar e implementar os requisitos de versionamento, tags e pull request;
- Desenvolver e documentar as etapas subsequentes do P0;
- Preparar o vídeo demonstrativo;
- Concluir as atividades de avaliação por pares previstas na capacitação.

## 8. Considerações parciais

Até esta etapa, o SciScreen demonstrou ser capaz de receber informações científicas, construir um prompt, consultar uma LLM e apresentar uma análise preliminar no terminal.

Os testes realizados demonstraram o tratamento de situações específicas de erro, incluindo ausência de credenciais, falhas de autenticação e problemas de comunicação.

A verificação em ambiente independente permitiu identificar uma limitação nos testes automatizados que não havia sido observada no ambiente original de desenvolvimento.

A correção implementada eliminou a dependência dos testes em relação à configuração local das credenciais, permitindo a aprovação dos quatro cenários avaliados na versão publicada do projeto.

Esse processo evidenciou um ciclo de desenvolvimento composto por implementação, teste, identificação de falha, diagnóstico, correção, versionamento e nova verificação.

O projeto permanece em desenvolvimento, com foco na consolidação da reprodutibilidade, na documentação das evidências e na conclusão dos requisitos da capacitação.
