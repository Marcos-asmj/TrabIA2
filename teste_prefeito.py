import unittest
from robo import *

class TesteQuemPrefeito(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_quem(self):
        mensagens = ["quem foi prefeito no ano de ?", "quem foi prefeito no ano ?"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O(s) prefeito(s) nesse ano foram:", resposta.text
            )

class TesteQualPrefeito(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_qual(self):
        mensagens = ["qual periodo foi prefeito?", "em qual periodo foi prefeito?", "qual periodo foi prefeito da Vitória da Conquista?"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "esteve no cargo durante esse período:", resposta.text
            )

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteQuemPrefeito))
    testes.addTest(carregador.loadTestsFromTestCase(TesteQualPrefeito))

    executor = unittest.TextTestRunner()
    executor.run(testes)