from arqLib.writeJSON import lerJSON, escreverJSON, adicionarMovimento, limparCarteira
from arqLib.writeTXT import atualizarArq
from time import localtime

ano = localtime()[0]
mes = localtime()[1]
dia = localtime()[2]

hoje = f'({dia}/{mes}/{ano})'

carteira = lerJSON('dados.json')

print("========================== CONTROLE DA CONTA ==========================\n")
print("""[ 1 ] Adicionar movimento
[ 2 ] Limpar carteira
[ 3 ] Ver contas
[ 4 ] Ver carteira inteira
[ 5 ] Adicionar gasto
[ 6 ] Adicionar deposito
""")

opcao = int(input('O que deseja fazer? '))

if opcao == 1:

    novo_movimento = {'nome': str(input('Qual foi o movimento? ')),
                      'valor': float(input('Valor do movimento: ')),
                      "data": hoje}
    carteira['saldo'] += novo_movimento['valor']

    if novo_movimento['valor'] > carteira['gastoMaisAlto']['valor']:
        carteira['gastoMaisAlto'] = novo_movimento

    adicionarMovimento('dados.json', carteira, novo_movimento)
    escreverJSON('dados.json', carteira)
    atualizarArq('arquivo', carteira)

elif opcao == 2:
    limparCarteira('dados.json', carteira)
    atualizarArq('arquivo', carteira)

elif opcao == 3:
    print("""[ 1 ] Registrar conta
[ 2 ] Pagar conta\n""")

    escolha = int(input('O que deseja fazer?' ))

    if escolha == 1:
        nomeConta = str(input('\nQual o nome da conta? '))
        valorConta = float(input('Qual o valor da conta? '))

        nova_conta = {"nome": nomeConta, "valor": valorConta, "pago": False}

        carteira['contas'].append(nova_conta)

        escreverJSON('dados.json', carteira)

    elif escolha == 2:
        contador = 1
        for conta in carteira["contas"]:
            print(f'[ {contador} ] {conta["nome"]}: R${conta["valor"]} ', end='')
            if not conta['pago']:
                print('[ NÃO PAGO ]')
            else:
                print('[ PAGO ]')
            contador += 1

        IDcontaPagar = int(input('\nQual conta deseja pagar?'))

        contaPagar = carteira['contas'][IDcontaPagar - 1]

        print(contaPagar)

        contaPagar['pago'] = True

        novo_movimento = {"nome": contaPagar["nome"], "valor": contaPagar["valor"], "data": hoje}

        carteira['movimentos'].append(novo_movimento)

        carteira['saldo'] -= novo_movimento['valor']

        escreverJSON('dados.json', carteira)

elif opcao == 4:
    print("============== Movimento Financeiro ==============")
    print(f'Saldo: R${carteira["saldo"]}\n')
    print('Contas:')
    for conta in carteira['contas']:
        print(f'{conta["nome"]}: R${conta["valor"]}')
    print()
    print('Movimentos: ')
    for movimento in carteira['movimentos']:
        print(f'{movimento["data"]} {movimento["nome"]}: R${movimento["valor"]}')

elif opcao == 5:
    novo_gasto = {"nome": str(input('Nome do gasto: ')), "valor": float(input('Valor do gasto: ')), "data": hoje}
    carteira['gastos'].append(novo_gasto)
    carteira['saldo'] -= novo_gasto['valor']
    carteira['movimentos'].append(novo_gasto)

    escreverJSON('dados.json', carteira)

elif opcao == 6:
    novo_deposito = {"nome": str(input('Nome do deposito: ')), "valor": float(input('Valor do deposito: ')), "data": hoje}
    carteira['saldo'] += novo_deposito['valor']
    carteira['depositos'].append(novo_deposito)
    carteira['movimentos'].append(novo_deposito)

    escreverJSON('dados.json', carteira)

input('\nQualquer tecla para terminar: ')
