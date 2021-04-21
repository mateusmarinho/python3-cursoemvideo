'''Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros:
 início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
 a) de 1 até 10, de 1 em 1
 b) de 10 até 0, de 2 em 2
 c) uma contagem personalizada'''

from time import sleep


def linha(n):
    print('-=' * n)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim < inicio:
        fim -= 1
        passo *= -1
    else:
        fim += 1
    for i in range(inicio, fim, passo):
        sleep(0.5)
        print(f'{i}  ', end='')
    print('FIM!')


# Programa principal
linha(30)
contador(1, 10, 1)
linha(30)
contador(10, 0, 2)
linha(30)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
linha(30)
contador(i, f, p)
