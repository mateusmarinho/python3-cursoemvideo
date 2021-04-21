total = cont = menorpreco = contmil = 0
while True:
    print('-=' * 20)
    print('{:^40}'.format('NOVO PRODUTO'))
    print('-=' * 20)
    nome = input('Digite o nome do produto: ').strip().upper()
    preco = float(input('Digite o preço do produto: R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        contmil += 1
    if cont == 1 or preco < menorpreco:
        menorpreco = preco
        maisbarato = nome
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if resposta == 'N':
        break
print('--'*20)
print(f'Total da compra: R$ {total:.2f}')
print(f'{contmil} produtos custaram mais de R$ 1000,00')
print(f'O produto mais barato foi {maisbarato} que custa R$ {menorpreco:.2f}')
