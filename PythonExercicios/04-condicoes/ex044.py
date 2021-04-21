valor = float(input('Digite o valor da compra: R$ '))
print('''Condições de pagamento:
[1] pagto. à vista no dinheiro ou cheque
[2] pagto. à vista no cartão
[3] pagto. em até 2x no cartão
[4] pagto. em 3x ou mais no cartão''')
cond = int(input('Escolha a forma de pagamento: '))
if cond == 1:
    total = 0.90 * valor
    print('Valor a pagar: R$ {:.2f}'.format(total))
elif cond == 2:
    total = 0.95 * valor
    print('Valor a pagar: R$ {:.2f}'.format(total))
elif cond == 3:
    print('Valor a pagar: 2 x R$ {:.2f} = R$ {:.2f}'.format(valor / 2, valor))
elif cond == 4:
    total = 1.20 * valor
    parc = int(input('Número de parcelas: '))
    print('Valor a pagar: {} x R$ {:.2f} = R$ {:.2f}'.format(parc, total / parc, total))
else:
    print('Opção inválida!')
