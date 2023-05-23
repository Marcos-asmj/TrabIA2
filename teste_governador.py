import unittest
from robo import *

class TesteQuemGovernador(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_quem(self):
        mensagens = ["quem foi governador no ano de ?", "quem foi governador no ano ?"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O(s) governador(es) nesse ano foram:", resposta.text
            )

class TesteQualGovernador(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_qual(self):
        mensagens = ["qual periodo foi governador?", "em qual periodo foi governador?", "qual periodo foi governador da Bahia?"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "esteve no cargo durante esse período:", resposta.text
            )

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteQuemGovernador))
    testes.addTest(carregador.loadTestsFromTestCase(TesteQualGovernador))

    executor = unittest.TextTestRunner()
    executor.run(testes)