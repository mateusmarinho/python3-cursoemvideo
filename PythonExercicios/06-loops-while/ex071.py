print('-='*20)
print('{:^40}'.format('BANCO MATEUS'))
print('-='*20)
valor = int(input('Qual valor você deseja sacar? R$ '))
total = valor
cedula = 50
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Quant. de cédulas de R$ {cedula} = {totced}')
        totced = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if total == 0:
            break
print('Fim da operação!')
