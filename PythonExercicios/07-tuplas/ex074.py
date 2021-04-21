'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

tupla = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))
print(f'Números gerados: {tupla}')
print(f'O maior valor gerado foi: {max(tupla)}')
print(f'O menor valor gerado foi: {min(tupla)}')
