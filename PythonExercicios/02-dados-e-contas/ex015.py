d = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
print('O valor a pagar é R$ {:.2f}'.format(60 * d + 0.15 * km))
