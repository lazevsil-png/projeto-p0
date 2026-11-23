
import os
from dotenv import load_dotenv
from google import genai

# Carrega as variaveis do arquivo .env
load_dotenv()

# Recupera a chave da API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERRO: Chave GEMINI_API_KEY nao encontrada.")
    raise SystemExit(1)

# Conecta ao Gemini
client = genai.Client(api_key=api_key)

print("Enviando mensagem ao Gemini...")

try:
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents="Responda em portugues: o que e um resumo cientifico? Use apenas uma frase."
    )

    print("\nResposta do Gemini:")
    print(response.text)

except Exception as erro:
    print("\nNao foi possivel concluir a chamada ao Gemini.")
    print("Tipo de erro:", type(erro).__name__)
    print("Detalhes:", str(erro))
