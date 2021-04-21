from random import randint
from time import sleep
print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')
item = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)
pessoa = int(input('Qual é a sua jogada?: '))
if pessoa > 2 or pessoa < 0:
    print('Opção inválida!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(0.5)
    print('Eu escolhi: {}\nVocê escolheu: {}'.format(item[comp], item[pessoa]))
    if pessoa == comp:
        print('Empatamos!')
    elif pessoa == 0 and comp == 2:
        print('Você venceu!')
    elif pessoa == 1 and comp == 0:
        print('Você venceu!')
    elif pessoa == 2 and comp == 1:
        print('Você venceu!')
    else:
        print('Você perdeu!')
