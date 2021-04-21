valor = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário do comprador: R$ '))
anos = int(input('Em quantos anos pretende pagar a casa? '))
prest = valor / (anos * 12)
print('Valor da prestação mensal: R$ {:.2f}'.format(prest))
if prest <= 0.30 * salario:
    print('Empréstimo CONCEDIDO.')
else:
    print('Empréstimo NEGADO.')
