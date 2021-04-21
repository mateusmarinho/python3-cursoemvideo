'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
 com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles
 é o maior.'''
from time import sleep


def linha(n):
    print('-=' * n)


def maior(* num):
    linha(30)
    tam = len(num)
    print('Analisando os valores passados...')
    if tam == 0:
        sleep(0.5)
        print('Nenhum valor foi informado. Não existe um valor maior.')
    else:
        for n in num:
            sleep(0.5)
            print(f'{n} ', end='')
        sleep(0.5)
        print(f'\nForam informados {tam} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
