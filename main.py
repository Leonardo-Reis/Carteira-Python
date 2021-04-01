from meu_json import lerJSON, escreverJSON

carteira = lerJSON('dados.json')

novo_movimento = {'nome': str(input('Qual foi o movimento? ')), 'valor': int(input('Valor do movimento: '))}

carteira['saldo'] += novo_movimento['valor']

carteira['movimentos'][2] = carteira['movimentos'][1]
carteira['movimentos'][1] = carteira['movimentos'][0]
carteira['movimentos'][0] = novo_movimento

escreverJSON('dados.json', carteira)
