'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos
pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[], [], []]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin].append(int(input(f'Digite um valor para a posição [{lin},{col}]: ')))

print('-='*40)
for linha in matriz:
    print(f'[{linha[0]:^5}][{linha[1]:^5}][{linha[2]:^5}]')

#outra solução
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para a posição [{lin},{col}]: '))

print('-='*40)
for linha in matriz:
    print(f'[{linha[0]:^5}][{linha[1]:^5}][{linha[2]:^5}]')'''