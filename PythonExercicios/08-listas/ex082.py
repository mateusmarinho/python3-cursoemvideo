'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = input('Deseja continuar [S/N]?: ').strip()
    if resp in 'Nn':
        break
for n in numeros:
    if n % 2:
        impares.append(n)
    else:
        pares.append(n)
print(f'Lista completa: {numeros}')
print(f'Lista de pares: {pares}')
print(f'Lista de ímpares: {impares}')
