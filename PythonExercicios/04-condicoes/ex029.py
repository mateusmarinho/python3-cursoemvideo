v = float(input('Digite a velocidade do carro: '))
if v > 80:
    print('O limite de 80 km/h foi excedido. Multa: R$ {:.2f}'.format(7 * (v - 80)))
print('Dirija com segurança!')
