def escreverLinha(arquivo: str, conteudo: str):
    with open(f'{arquivo}.txt', 'a') as arquivo:
        arquivo.write(conteudo)
        arquivo.close()


def atualizarArq(arquivo, objeto: object):
    with open(f'{arquivo}.txt', 'w') as arq:
        arq.write(f'Saldo: {objeto["saldo"]} \n')
        arq.write('\n')
        arq.write('Ultimos movimentos: \n')
        arq.write('\n')
        arq.close()
    for movimento in objeto['movimentos']:
        escreverLinha(arquivo, f'{movimento["nome"]}: {movimento["valor"]}\n')
