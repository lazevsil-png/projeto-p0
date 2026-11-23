

\# SciScreen — Relatório de Execução



\## 1. Identificação do projeto



\*\*Projeto:\*\* SciScreen — Triagem Científica Assistida por LLM



\*\*Capacitação:\*\* Instituto Hardware BR — P0: Primeiro fluxo com LLM



\*\*Linguagem:\*\* Python 3.13



\*\*Interface:\*\* Terminal



\*\*Provedor de LLM:\*\* GroqCloud



\*\*Modelo utilizado:\*\* openai/gpt-oss-20b



\*\*Repositório:\*\* https://github.com/lazevsil-png/projeto-p0



\## 2. Problema identificado



A seleção de artigos científicos para revisões de literatura exige a leitura de resumos e a comparação de seu conteúdo com objetivos e critérios previamente definidos.



Esse processo pode ser repetitivo e consumir tempo, especialmente quando envolve muitos artigos.



O SciScreen foi desenvolvido como uma ferramenta experimental para auxiliar na triagem preliminar de resumos científicos, sem substituir a avaliação crítica do pesquisador.



\## 3. Solução proposta



O SciScreen é uma aplicação Python executada pelo terminal.



O usuário informa:



\- O objetivo da revisão de literatura;

\- Os critérios de inclusão e exclusão;

\- O resumo científico (abstract) a ser analisado.



A aplicação organiza essas informações em um prompt estruturado e o envia a um modelo de linguagem por meio de uma API.



O modelo retorna uma análise textual que auxilia o pesquisador a avaliar a possível relevância do artigo.



A decisão final de inclusão ou exclusão permanece sob responsabilidade humana.



\## 4. Evolução do desenvolvimento



\### 4.1. Nível Básico — Primeiro fluxo com LLM



O desenvolvimento começou com a criação de uma aplicação Python capaz de receber entradas textuais pelo terminal.



Foram implementadas a leitura dos campos, a validação de entradas obrigatórias e a construção de um prompt para análise científica.



Inicialmente, foram realizados experimentos de integração com a API do Google Gemini. Durante os testes, ocorreram dificuldades de disponibilidade e acesso aos modelos.



Posteriormente, a integração foi realizada com o GroqCloud, utilizando o modelo openai/gpt-oss-20b.



A aplicação conseguiu enviar um prompt real à LLM e apresentar a resposta no terminal, demonstrando o funcionamento do fluxo principal.



As credenciais foram armazenadas em um arquivo .env, excluído do controle de versão por meio do .gitignore.



O arquivo .env.example foi atualizado para indicar as variáveis necessárias à configuração do projeto.



\### 4.2. Testes e tratamento de falhas



Foram realizados testes manuais e automatizados para verificar o comportamento da aplicação.



\*\*Testes manuais:\*\*



\- Execução do fluxo principal com uma chamada real à LLM;

\- Validação de campos vazios;

\- Simulação de credencial ausente;

\- Simulação de credencial inválida;

\- Simulação de falha de comunicação.



\*\*Testes automatizados:\*\*



Foi criado o arquivo test\_llm\_service.py, utilizando a biblioteca unittest e simulações com unittest.mock.



Foram verificados quatro cenários:



1\. Ausência da chave de API;

2\. Erro de autenticação HTTP 401;

3\. Falha de comunicação;

4\. Retorno de uma resposta válida da LLM.



\*\*Resultado observado:\*\*



Ran 4 tests in 0.004s



OK



Os quatro testes automatizados foram aprovados no ambiente de desenvolvimento.



Esses testes não realizam chamadas reais à API e podem ser executados novamente por outros desenvolvedores.



\## 5. Decisões técnicas



A aplicação utiliza Python por sua simplicidade e disponibilidade de bibliotecas para integração com serviços de LLM.



A interface por terminal foi escolhida para manter o escopo compatível com o objetivo do P0, sem acrescentar complexidade de interface gráfica.



A separação entre construção do prompt, integração com a API e execução principal facilita a manutenção e os testes.



O uso de variáveis de ambiente evita inserir credenciais diretamente no código-fonte.



Os testes com simulações permitem verificar situações de falha sem depender da disponibilidade do serviço externo.



\## 6. Limitações identificadas



O SciScreen não realiza uma avaliação científica definitiva dos artigos.



As respostas da LLM podem apresentar erros de interpretação, omissões ou classificações inadequadas.



A qualidade da análise depende da clareza dos critérios fornecidos pelo usuário e do conteúdo do resumo.



O funcionamento com chamadas reais depende da disponibilidade do provedor, da validade da credencial e dos limites de utilização da API.



Os testes automatizados verificam comportamentos específicos do código, mas não validam a precisão científica das classificações.



\## 7. Próximas etapas



As seguintes atividades ainda precisam ser verificadas ou concluídas:



\- Testar a instalação em um ambiente limpo;

\- Revisar e completar o README;

\- Documentar exemplos de entrada e saída;

\- Organizar as evidências dos níveis da capacitação;

\- Verificar os requisitos de versionamento, tags e pull request;

\- Preparar o vídeo demonstrativo;

\- Concluir as atividades de avaliação por pares previstas na capacitação.



\## 8. Considerações parciais



Até esta etapa, o SciScreen demonstrou ser capaz de receber informações científicas, construir um prompt, consultar uma LLM e apresentar uma análise preliminar no terminal.



Os testes realizados também demonstraram o tratamento de situações específicas de erro.



O projeto permanece em desenvolvimento, com foco na reprodutibilidade, documentação e conclusão dos requisitos da capacitação.



