
import unittest
from unittest.mock import patch

import httpx
from groq import APIConnectionError, APIStatusError, APITimeoutError

from llm_service import analisar_resumo


class TestSciScreen(unittest.TestCase):

    @patch("llm_service.os.getenv", return_value=None)
    def test_chave_ausente(self, mock_getenv):
        resultado = analisar_resumo("Teste")

        self.assertEqual(
            resultado,
            "ERRO: Chave da API nao configurada."
        )

    @patch("llm_service.os.getenv", return_value="chave_ficticia")
    @patch("llm_service.Groq")
    def test_credencial_invalida(self, mock_groq, mock_getenv):
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

    @patch("llm_service.os.getenv", return_value="chave_ficticia")
    @patch("llm_service.Groq")
    def test_falha_comunicacao(self, mock_groq, mock_getenv):
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

    @patch("llm_service.os.getenv", return_value="chave_ficticia")
    @patch("llm_service.Groq")
    def test_resposta_valida(self, mock_groq, mock_getenv):
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


    @patch("llm_service.os.getenv", return_value="   ")
    def test_configuracao_invalida(self, mock_getenv):
        resultado = analisar_resumo("Teste")

        self.assertEqual(
            resultado,
            "ERRO: Chave da API nao configurada."
        )

    @patch("llm_service.os.getenv", return_value="chave_ficticia")
    @patch("llm_service.Groq")
    def test_servico_indisponivel(self, mock_groq, mock_getenv):
        resposta = httpx.Response(
            503,
            request=httpx.Request("POST", "https://api.groq.com")
        )

        erro = APIStatusError(
            "Servico indisponivel",
            response=resposta,
            body=None
        )

        mock_groq.return_value.chat.completions.create.side_effect = erro

        resultado = analisar_resumo("Teste")

        self.assertEqual(
            resultado,
            "ERRO: Servico temporariamente indisponivel."
        )

    @patch("llm_service.os.getenv", return_value="chave_ficticia")
    @patch("llm_service.Groq")
    def test_limite_requisicoes(self, mock_groq, mock_getenv):
        resposta = httpx.Response(
            429,
            request=httpx.Request("POST", "https://api.groq.com")
        )

        erro = APIStatusError(
            "Limite atingido",
            response=resposta,
            body=None
        )

        mock_groq.return_value.chat.completions.create.side_effect = erro

        resultado = analisar_resumo("Teste")

        self.assertEqual(
            resultado,
            "ERRO: Limite de requisicoes atingido."
        )

    @patch("llm_service.os.getenv", return_value="chave_ficticia")
    @patch("llm_service.Groq")
    def test_timeout(self, mock_groq, mock_getenv):
        erro = APITimeoutError(
            request=httpx.Request("POST", "https://api.groq.com")
        )

        mock_groq.return_value.chat.completions.create.side_effect = erro

        resultado = analisar_resumo("Teste")

        self.assertEqual(
            resultado,
            "ERRO: Tempo limite de resposta da API excedido."
        )

    @patch("llm_service.os.getenv", return_value="chave_ficticia")
    @patch("llm_service.Groq")
    def test_resposta_vazia(self, mock_groq, mock_getenv):
        mock_groq.return_value.chat.completions.create.return_value.choices = [
            type(
                "Choice",
                (),
                {
                    "message": type(
                        "Message",
                        (),
                        {"content": ""}
                    )()
                }
            )()
        ]

        resultado = analisar_resumo("Teste")

        self.assertEqual(
            resultado,
            "ERRO: A LLM retornou uma resposta vazia."
        )

    @patch("llm_service.os.getenv", return_value="chave_ficticia")
    @patch("llm_service.Groq")
    def test_resposta_inesperada(self, mock_groq, mock_getenv):
        mock_groq.return_value.chat.completions.create.return_value.choices = []

        resultado = analisar_resumo("Teste")

        self.assertEqual(
            resultado,
            "ERRO: A LLM retornou uma resposta em formato inesperado."
        )


if __name__ == "__main__":
    unittest.main()
