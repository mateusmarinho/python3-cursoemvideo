'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

pessoas = list()
dados = list()
menor_peso = maior_peso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        menor_peso = maior_peso = dados[1]
    else:
        if dados[1] < menor_peso:
            menor_peso = dados[1]
        if dados[1] > maior_peso:
            maior_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]: ')).strip()
    if resp in 'Nn':
        break
print('-='*40)
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior_peso:.2f} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi {menor_peso:.2f} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')
