'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de
um terreno retangular (largura e comprimento) e mostre a área do terreno.'''


def titulo(msg):
    print(f'{msg:^30}')
    print('-' * 30)


def areaTerreno(a, b):
    area = a * b
    print(f'A área de um terreno {a} x {b} é de {area:.2f} m².')
    

# Programa principal
titulo('Controle de Terrenos')
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
areaTerreno(larg, comp)
