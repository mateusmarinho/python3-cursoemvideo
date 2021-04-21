from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
n1 = randint(0, 5) # a máquina escolhe um inteiro aleatório entre 0 e 5
n2 = int(input('Em que número pensei?: ')) # usuário tenta adivinhar
print('PROCESSANDO...')
sleep(3)
print('Parabéns! Você acertou!' if n1 == n2 else 'Que pena! Você errou!')
