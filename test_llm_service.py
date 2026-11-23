
import unittest
from unittest.mock import patch

import httpx
from groq import APIConnectionError, APIStatusError

from llm_service import analisar_resumo


class TestSciScreen(unittest.TestCase):

    @patch("llm_service.os.getenv", return_value=None)
    def test_chave_ausente(self, mock_getenv):
        resultado = analisar_resumo("Teste")

        self.assertEqual(
            resultado,
            "ERRO: Chave da API nao configurada."
        )

    @patch("llm_service.Groq")
    def test_credencial_invalida(self, mock_groq):
        resposta = httpx.Response(
            401,
            request=httpx.Request(
                "POST",
                "https://api.groq.com"
            )
        )

        erro = APIStatusError(
            "Credencial invalida",
            response=resposta,
            body=None
        )

        mock_groq.return_value.chat.completions.create.side_effect = erro

        resultado = analisar_resumo("Teste")

        self.assertEqual(
            resultado,
            "ERRO: Problema de autenticacao ou permissao."
        )

    @patch("llm_service.Groq")
    def test_falha_comunicacao(self, mock_groq):
        erro = APIConnectionError(
            request=httpx.Request(
                "POST",
                "https://api.groq.com"
            )
        )

        mock_groq.return_value.chat.completions.create.side_effect = erro

        resultado = analisar_resumo("Teste")

        self.assertEqual(
            resultado,
            "ERRO: Falha de conexao com a API."
        )

    @patch("llm_service.Groq")
    def test_resposta_valida(self, mock_groq):
        mock_groq.return_value.chat.completions.create.return_value.choices = [
            type(
                "Choice",
                (),
                {
                    "message": type(
                        "Message",
                        (),
                        {"content": "Artigo potencialmente relevante."}
                    )()
                }
            )()
        ]

        resultado = analisar_resumo("Teste")

        self.assertEqual(
            resultado,
            "Artigo potencialmente relevante."
        )


if __name__ == "__main__":
    unittest.main()
