
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

chave = os.getenv("GROQ_API_KEY")

if not chave:
    raise RuntimeError("GROQ_API_KEY não encontrada no .env")

cliente = Groq(api_key=chave)

resposta = cliente.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Responda em português: o que é química analítica? Use apenas uma frase."
        }
    ],
    temperature=0.2,
    max_completion_tokens=150,
)

print("\nResposta da LLM:")
print(resposta.choices[0].message.content)
