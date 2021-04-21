'''Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro
da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados
pela função anterior.'''
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for i in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        sleep(0.5)
        print(f'{num}  ', end='')
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos {soma}.')


# Programa principal
numeros = []
sorteia(numeros)
somaPar(numeros)
