
import os

from dotenv import load_dotenv
from groq import Groq, APIStatusError, APIConnectionError, APITimeoutError

load_dotenv()

MODELO = "openai/gpt-oss-20b"
TIMEOUT = 30.0
TEMPERATURA = 0.2
MAX_TOKENS = 1500


def carregar_configuracao():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key or not api_key.strip():
        return None

    return api_key.strip()


def consultar_llm(prompt, api_key):
    client = Groq(
        api_key=api_key,
        timeout=TIMEOUT
    )

    return client.chat.completions.create(
        model=MODELO,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=TEMPERATURA,
        max_completion_tokens=MAX_TOKENS
    )


def extrair_resposta(resposta):
    try:
        texto = resposta.choices[0].message.content

    except (AttributeError, IndexError, TypeError):
        return "ERRO: A LLM retornou uma resposta em formato inesperado."

    if texto is None:
        return "ERRO: A LLM retornou uma resposta vazia."

    if not isinstance(texto, str):
        return "ERRO: A LLM retornou uma resposta em formato inesperado."

    if not texto.strip():
        return "ERRO: A LLM retornou uma resposta vazia."

    return texto


def analisar_resumo(prompt):
    api_key = carregar_configuracao()

    if not api_key:
        return "ERRO: Chave da API nao configurada."

    try:
        resposta = consultar_llm(prompt, api_key)
        return extrair_resposta(resposta)

    except APIStatusError as erro:
        if erro.status_code in (500, 502, 503, 504):
            return "ERRO: Servico temporariamente indisponivel."

        if erro.status_code == 429:
            return "ERRO: Limite de requisicoes atingido."

        if erro.status_code in (401, 403):
            return "ERRO: Problema de autenticacao ou permissao."

        return f"ERRO: Falha na API (codigo {erro.status_code})."

    except APITimeoutError:
        return "ERRO: Tempo limite de resposta da API excedido."

    except APIConnectionError:
        return "ERRO: Falha de conexao com a API."

    except Exception:
        return "ERRO: Falha inesperada na comunicacao."
