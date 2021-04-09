from arqLib.writeJSON import lerJSON, escreverJSON, limparCarteira
from time import localtime

ano = localtime()[0]
mes = localtime()[1]
dia = localtime()[2]

hoje = f'({dia}/{mes}/{ano})'

carteira = lerJSON('dados.json')

print("========================== CONTROLE DA CONTA ==========================\n")
print("""[ 1 ] Ver Carteira
[ 2 ] Limpar carteira
[ 3 ] Ver contas
[ 4 ] Adicionar movimento
[ 5 ] Adicionar gasto
[ 6 ] Adicionar deposito
""")

opcao = int(input('O que deseja fazer? '))

if opcao == 4:  # Adicionar movimento

    print('kkk')

elif opcao == 2:  # Limpar carteira
    limparCarteira('dados.json', carteira)

elif opcao == 3:  # Ver contas
    print("""[ 1 ] Registrar conta
[ 2 ] Pagar conta\n""")

    escolha = int(input('O que deseja fazer? '))

    if escolha == 1:
        nomeConta = str(input('\nQual o nome da conta? ')).strip().capitalize()
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

        contaPagar['pago'] = True

        novo_movimento = {"nome": contaPagar["nome"],
                          "valor": contaPagar["valor"],
                          "data": hoje}

        carteira['movimentos'].append(novo_movimento)
        carteira['gastos'].append(novo_movimento)

        carteira['saldo'] -= novo_movimento['valor']

        escreverJSON('dados.json', carteira)

elif opcao == 1:  # Ver carteira
    print("============== Movimento Financeiro ==============")
    print(f'Saldo: R${carteira["saldo"]:.2f}\n')
    print('Contas =================================')
    for conta in carteira['contas']:
        print(f'{conta["nome"]}: R${conta["valor"]}', end=' ')
        if conta['pago']:
            print('[ PAGO ]')
        else:
            print('[ NÃO PAGO ]')
    print()
    print('Depositos ==============================')
    for deposito in carteira['depositos']:
        print(f'{deposito["data"]} {deposito["nome"]}: R${deposito["valor"]}')
    print()
    print('Gastos =================================')
    for gasto in carteira['gastos']:
        print(f'{gasto["data"]} {gasto["nome"]}: R${gasto["valor"]}')

elif opcao == 5:  # Gasto
    novo_gasto = {"nome": str(input('Nome do gasto: ')).strip().capitalize(),
                  "valor": float(input('Valor do gasto: ')),
                  "data": hoje}
    carteira['gastos'].append(novo_gasto)
    carteira['saldo'] -= novo_gasto['valor']
    carteira['movimentos'].append(novo_gasto)

    if novo_gasto['valor'] > carteira['gastoMaisAlto']['valor']:
        carteira['gastoMaisAlto'] = novo_gasto

    escreverJSON('dados.json', carteira)

elif opcao == 6:  # Deposito
    novo_deposito = {"nome": str(input('Nome do deposito: ')).strip().capitalize(),
                     "valor": float(input('Valor do deposito: ')),
                     "data": hoje}
    carteira['saldo'] += novo_deposito['valor']
    carteira['depositos'].append(novo_deposito)
    carteira['movimentos'].append(novo_deposito)

    escreverJSON('dados.json', carteira)

input('\nQualquer tecla para terminar: ')
