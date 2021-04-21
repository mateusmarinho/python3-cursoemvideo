num = int(input('Digite um número de 0 a 9999: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhares: {}'.format(m))
