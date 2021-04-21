'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[], [], []]
soma_par = soma_3acol = maior_2alin = 0
for lin in range(0, 3):
    for col in range(0, 3):
        num = int(input(f'Digite um valor para a posição [{lin},{col}]: '))
        matriz[lin].append(num)
        if num % 2 == 0:
            soma_par += num
        if col == 2:
            soma_3acol += num
        if lin == 1:
            if col == 0:
                maior_2alin = num
            elif num > maior_2alin:
                maior_2alin = num

print('-='*40)
for linha in matriz:
    print(f'[{linha[0]:^5}][{linha[1]:^5}][{linha[2]:^5}]')
print('-='*40)
print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_3acol}')
print(f'O maior valor da segunda linha é {maior_2alin}')
