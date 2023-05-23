from chatterbot import ChatBot
from difflib import SequenceMatcher
import json

CONFIANCA_MINIMA = 0.50
DADOS = "C:/Users/Marcos/Documents/labs/TrabIA2/dados.json"

def comparar_mensagens(mensagem_digitada, mensagem_candidata):
    confianca = 0.0

    digitada = mensagem_digitada.text
    candidata = mensagem_candidata.text
    if digitada and candidata:
        confianca = SequenceMatcher(None, 
            digitada,
            candidata)
        confianca = round(confianca.ratio(), 2)

    return confianca

def iniciar():
    robo = ChatBot("Maria",
                   read_only=True,
                   statement_comparison_function=comparar_mensagens,     
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                   ])

    return robo

def encontrar_cargo(mensagem):
    cargo_encontrado = ''

    with open(DADOS, encoding='utf-8') as arquivo_de_dados:
        dados = json.load(arquivo_de_dados)
        for cargo in dados:
            if cargo.casefold() in mensagem.casefold():
                cargo_encontrado = cargo
        arquivo_de_dados.close()

    return cargo_encontrado

def encontrar_nome(mensagem, cargo):
    nome = ''
    encontrado = False

    with open(DADOS, encoding='utf-8') as arquivo_de_dados:
        dados = json.load(arquivo_de_dados)
        for dado in dados[cargo]:
            if dado["nome"].casefold() in mensagem.casefold():
                nome = dado["nome"]
                encontrado = True
        arquivo_de_dados.close()

    return nome, encontrado

def formatar_mensagem(mensagem):
    cargo = encontrar_cargo(mensagem)
    nome, encontrado = encontrar_nome(mensagem, cargo)
    mensagem_treinada = ''

    with open(DADOS, encoding='utf-8') as arquivo_de_dados:
        dados = json.load(arquivo_de_dados)
        for dado in dados[cargo]:
            if nome == "":
                for ano in dado["periodo"]:
                    if ano in mensagem:
                        mensagem_treinada = mensagem.replace(ano, '')
            else:
                if dado["nome"].casefold() in mensagem.casefold():
                    mensagem_treinada = mensagem.replace(nome, '')
        arquivo_de_dados.close()

    return mensagem_treinada

def quem(mensagem):
    cargo = encontrar_cargo(mensagem)
    pessoas = []

    with open(DADOS, encoding='utf-8') as arquivo_de_dados:
        dados = json.load(arquivo_de_dados)
        for dado in dados[cargo]:
            for ano in dado["periodo"]:
                if ano in mensagem:
                    pessoas.append(dado["nome"])
        arquivo_de_dados.close()

    return pessoas

def qual(mensagem):
    cargo = encontrar_cargo(mensagem)
    nome, encontrado = encontrar_nome(mensagem, cargo)
    periodo = []

    with open(DADOS, encoding='utf-8') as arquivo_de_dados:
        dados = json.load(arquivo_de_dados)
        for dado in dados[cargo]:
            if nome.casefold() == dado["nome"].casefold():
                periodo = dado['periodo']
        arquivo_de_dados.close()

    if not encontrado:
        print(f"Não encontrei nenhum {cargo} com esse nome.")
        
    return periodo, nome

def executar_robo(robo):
    while True:
        mensagem = input("Digite alguma coisa... \n")
        mensagem_formatada = formatar_mensagem(mensagem)
        resposta = robo.get_response(mensagem_formatada.lower())
        print(f"o valor da confiança é: {resposta.confidence}")
        if (resposta.confidence >= CONFIANCA_MINIMA) and ('qual' in mensagem.casefold()):
            periodo, nome = qual(mensagem)
            if nome != "":
                print(">>", nome, resposta.text)
                for ano in periodo:
                    print(ano)
        elif(resposta.confidence >= CONFIANCA_MINIMA) and ('quem' in mensagem.casefold()):
            pessoas = quem(mensagem)
            if pessoas != []:
                print(">>", resposta.text)
                for pessoa in pessoas:
                    print(pessoa)
            else:
                print("Não encontrei historico deste cargo para esse ano")
        elif resposta.confidence >= CONFIANCA_MINIMA:
            print(">>", resposta.text)
        else:
            print("Infelizmente, ainda não sei responder isso")
            print("Pergunte outra coisa")


if __name__ == "__main__":
    robo = iniciar()

    executar_robo(robo)
