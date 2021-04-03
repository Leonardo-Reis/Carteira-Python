import json


def escreverJSON(arquivo: str, data: object):
    with open(f'{arquivo}', 'w') as json_file:
        json.dump(data, json_file)
        json_file.close()


def lerJSON(arquivo: str):
    with open(f'{arquivo}', 'r') as json_file:
        return json.load(json_file)


def adicionarMovimento(arquivo, carteira, movimento):
    carteira['movimentos'].append(movimento)
    escreverJSON(arquivo, carteira)


def limparCarteira(arquivo: str, carteira):
    carteira['saldo'] = 0
    carteira['movimentos'] = []
    carteira['gastoMaisAlto'] = {"nome": "", "valor": 0}
    carteira['contas'] = []
    carteira['gastos'] = []
    carteira['depositos'] = []
    escreverJSON(arquivo, carteira)
