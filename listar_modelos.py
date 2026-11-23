
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERRO: Chave da API nao encontrada.")
    raise SystemExit(1)

client = genai.Client(api_key=api_key)

try:
    print("Modelos disponiveis para generateContent:\n")

    for modelo in client.models.list():
        acoes = modelo.supported_actions or []

        if "generateContent" in acoes:
            print(modelo.name)

except Exception as erro:
    print("Erro ao consultar modelos.")
    print("Tipo:", type(erro).__name__)
    print("Detalhes:", str(erro))
