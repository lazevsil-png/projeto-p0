
import unittest
from prompt_sciscreen import criar_prompt


class TestSciScreen(unittest.TestCase):

    def test_prompt_contem_dados(self):
        prompt = criar_prompt(
            "Investigar residuos de disparo",
            "Incluir estudos experimentais",
            "Gunshot residue was analyzed using SEM-EDS."
        )

        self.assertIn(
            "Investigar residuos de disparo", prompt
        )
        self.assertIn(
            "Incluir estudos experimentais", prompt
        )
        self.assertIn(
            "Gunshot residue was analyzed", prompt
        )


if __name__ == "__main__":
    unittest.main()
