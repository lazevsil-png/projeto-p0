
import os

from dotenv import load_dotenv
from groq import Groq, APIStatusError, APIConnectionError, APITimeoutError

load_dotenv()


def analisar_resumo(prompt):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "ERRO: Chave da API nao configurada."

    try:
        client = Groq(api_key=api_key, timeout=30.0)

        resposta = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_completion_tokens=1500
        )

        texto = resposta.choices[0].message.content

        if not texto or not texto.strip():
            return "ERRO: A LLM retornou uma resposta vazia."

        return texto

    except APIStatusError as erro:
        if erro.status_code == 503:
            return "ERRO: Servico temporariamente indisponivel."

        if erro.status_code == 429:
            return "ERRO: Limite de requisicoes atingido."

        if erro.status_code in (401, 403):
            return "ERRO: Problema de autenticacao ou permissao."

        return f"ERRO: Falha na API (codigo {erro.status_code})."

    except (APIConnectionError, APITimeoutError):
        return "ERRO: Falha de conexao com a API."

    except Exception:
        return "ERRO: Falha inesperada na comunicacao."
