#mostra os 10 primeiros termos de uma PA
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print('Dez primeiros termos da PA:\n{}'.format(a1), end='  ')
for i in range(0, 9):
    a1 += r
    print('{}'.format(a1), end='  ')
