#MELHORANDO O EX028
from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
n1 = randint(0, 10) # a máquina escolhe um inteiro aleatório entre 0 e 10
chute = 0
acertou = False
while not acertou:
    n2 = int(input('Em que número pensei?: '))  # usuário tenta adivinhar
    print('PROCESSANDO...')
    sleep(3)
    chute += 1
    if n2 == n1:
        acertou = True
    elif n1 > n2:
        print('Mais... Tente novamente!')
    else:
        print('Menos... Tente novamente!')
print('Parabéns! Você acertou!\nNúmero de palpites = {}'.format(chute))
