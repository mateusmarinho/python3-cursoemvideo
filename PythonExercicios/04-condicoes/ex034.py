sal = float(input('Digite o salário do funcionário: R$ '))
if sal > 1250.00:
    print('O novo salário será R$ {:.2f}'.format(1.10 * sal))
else:
    print('O novo salário será R$ {:.2f}'.format(1.15 * sal))
