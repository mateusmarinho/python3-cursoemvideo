'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = input('Deseja continuar? [S/N]: ').strip()
    if resp in 'Nn':
        break
print('-='*30)
print(f'Foram digitados {len(numeros)} números.')
numeros.sort(reverse = True)
print(f'Os números digitados, em ordem decrescente foram: {numeros}')
if 5 in numeros:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')
