
import os

from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()


def analisar_resumo(prompt):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "ERRO: Chave da API nao configurada."

    try:
        client = genai.Client(api_key=api_key)

        resposta = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        if not resposta.text:
            return "ERRO: A LLM retornou uma resposta vazia."

        return resposta.text

    except errors.APIError as erro:
        if erro.code == 503:
            return (
                "ERRO: O Gemini esta temporariamente "
                "indisponivel. Tente novamente mais tarde."
            )

        if erro.code == 429:
            return "ERRO: Limite de requisicoes atingido."

        if erro.code in (401, 403):
            return "ERRO: Problema de autenticacao ou permissao."

        return f"ERRO: Falha na API (codigo {erro.code})."

    except Exception:
        return "ERRO: Falha inesperada na comunicacao."
