#soma de números pares digitados
s = 0
for i in range(0, 6):
    n = int(input('Digite o {}o. valor: '.format(i+1)))
    if n % 2 == 0:
        s += n
print('Soma dos números pares digitados: {}'.format(s))