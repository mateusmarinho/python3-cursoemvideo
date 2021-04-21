while True:
    print('-'*20)
    n = int(input('Quer ver a tabuada de qual valor? [Valor negativo para encerrar] : '))
    print('-'*20)
    if n < 0:
        break
    mult = 1
    while mult <= 10:
        print(f'{n} x {mult} = {n * mult}')
        mult += 1
print('Programa encerrado!')
