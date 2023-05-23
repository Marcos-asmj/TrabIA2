from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONVERSAS = [
    "C:/Users/Marcos/Documents/labs/TrabIA2/conversas/saudacoes.json",
    "C:/Users/Marcos/Documents/labs/TrabIA2/conversas/quem_presidente.json",
    "C:/Users/Marcos/Documents/labs/TrabIA2/conversas/quem_governador.json",
    "C:/Users/Marcos/Documents/labs/TrabIA2/conversas/quem_prefeito.json",
    "C:/Users/Marcos/Documents/labs/TrabIA2/conversas/qual_presidente.json",
    "C:/Users/Marcos/Documents/labs/TrabIA2/conversas/qual_governador.json",
    "C:/Users/Marcos/Documents/labs/TrabIA2/conversas/qual_prefeito.json"
]

def iniciar():
    robo = ChatBot("Maria")
    treinador = ListTrainer(robo)

    return treinador

def carregar_conversas():
    conversas = []

    for arquivo_conversas in CONVERSAS:
        with open(arquivo_conversas, "r", encoding='utf-8') as arquivo:
            conversas_para_treinamento = json.load(arquivo)
            conversas.append(conversas_para_treinamento["conversas"])

            arquivo.close()

    return conversas

def treinar(treinador, conversas):
    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagens = mensagens_resposta["mensagens"]
            resposta = mensagens_resposta["resposta"]

            print(f"treinando o robô. Mensagens: {mensagens}. Resposta: {resposta}")
            for mensagem in mensagens:
                treinador.train([mensagem, resposta])


if __name__ == "__main__":
    treinador = iniciar()

    conversas = carregar_conversas()
    if conversas:
        treinar(treinador, conversas)
