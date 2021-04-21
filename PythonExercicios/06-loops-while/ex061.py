# REFAZENDO O DESAFIO 51
# mostra os 10 primeiros termos de uma PA
print('GERADOR DE PA')
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print('Dez primeiros termos da PA:')
termo = a1
i = 1
while i <= 10:
    print('{}  '.format(termo), end='')
    termo += r
    i += 1
print('\nFIM')
