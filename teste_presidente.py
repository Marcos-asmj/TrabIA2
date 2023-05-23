import unittest
from robo import *

class TesteQuemPresidente(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_quem(self):
        mensagens = ["quem foi presidente no ano de ?", "quem foi presidente no ano ?"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O(s) presidente(s) nesse ano foram:", resposta.text
            )

class TesteQualPresidente(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_qual(self):
        mensagens = ["qual periodo foi presidente?", "em qual periodo foi presidente?", "qual periodo foi presidente do Brasil?"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "esteve no cargo durante esse período:", resposta.text
            )

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteQuemPresidente))
    testes.addTest(carregador.loadTestsFromTestCase(TesteQualPresidente))

    executor = unittest.TextTestRunner()
    executor.run(testes)