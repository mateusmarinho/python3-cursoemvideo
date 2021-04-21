'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

numeros = []
for cont in range(0, 5):
    numeros.append(int(input(f'Digite um número para a posição {cont}: ')))
print(f'Você digitou os números: {numeros}')
print(f'O maior valor digitado foi {max(numeros)} e está na(s) posição(ões): ', end='')
for i, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{i}.. ', end='')
print(f'\nO menor valor digitado foi {min(numeros)} e está na(s) posição(ões): ', end='')
for i, v in enumerate(numeros):
    if v == min(numeros):
        print(f'{i}.. ', end='')
