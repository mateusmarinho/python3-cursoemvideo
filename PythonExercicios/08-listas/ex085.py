'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares
e ímpares em ordem crescente.'''

numeros = [[], []]
for i in range(0, 7):
    num = int(input(f'Digite o {i+1}º valor: '))
    if num % 2 == 0: #condição se for ímpar
        numeros[0].append(num)
    else: #condição se for par
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('-='*40)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
