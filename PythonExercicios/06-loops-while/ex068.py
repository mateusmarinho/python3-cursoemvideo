from random import randint
from time import sleep
vitorias = 0
while True:
    print('-='*20)
    print('PAR OU ÍMPAR')
    print('-='*20)
    computador = randint(0, 5)
    opcao = int(input('''Escolha:
    [ 1 ] PAR
    [ 2 ] ÍMPAR
    Digite sua opção: '''))
    jogador = int(input('Escolha um número de 0 a 5: '))
    soma = computador + jogador
    if soma % 2 == 0:
        resultado = 1
        nome_res = 'PAR'
    else:
        resultado = 2
        nome_res = 'ÍMPAR'
    print(f'Você jogou: {jogador}. Eu joguei: {computador}. Total: {soma}')
    sleep(1)
    print(f'{soma} é {nome_res}!')
    if opcao == resultado:
        print('Parabéns! Você ganhou!')
        sleep(1)
        vitorias += 1
    else:
        print('Que pena! Você perdeu!')
        sleep(1)
        break
print('-'*20)
print(f'Total de vitórias: {vitorias}')
print('-'*20)
