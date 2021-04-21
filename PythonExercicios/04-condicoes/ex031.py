d = float(input('Digite a distância da viagem em km: '))
if d <= 200:
    print('Preço da passagem: R$ {:.2f}'.format(0.50 * d))
else:
    print('Preço da passagem: R$ {:.2f}'.format(0.45 * d))
