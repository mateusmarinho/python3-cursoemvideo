'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
serão exibidos todos os valores únicos digitados, em ordem crescente.'''

numeros = []
while True:
    num = int(input('Digite um valor: '))
    if num in numeros:
        print('Valor duplicado! Não foi adicionado!')
    else:
        numeros.append(num)
        print('Valor adicionado!')
    resp = input('Deseja continuar? [S/N]: ').strip()
    if resp in 'Nn':
        break
numeros.sort()
print('-='*20)
print(f'Valores digitados: {numeros}')
