'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep

print('-'*40)
print('APOSTA MEGA SENA')
print('-'*40)
aposta = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie?: '))
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for c in range(0, quant):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in aposta:
            aposta.append(num)
            cont += 1
        if cont >= 6:
            break
    aposta.sort()
    jogos.append(aposta[:])
    aposta.clear()
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print('BOA SORTE!')