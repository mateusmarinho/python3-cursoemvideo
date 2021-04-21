#TRIÂNGULOS v2.0
print('-=-'*20)
print('Analisando triângulos')
print('-=-'*20)
r1 = float(input('Digite o comprimento do primeiro segmento: '))
r2 = float(input('Digite o comprimento do segundo segmento: '))
r3 = float(input('Digite o comprimento do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos formam um triângulo')
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('O triângulo é ESCALENO.')
    else:
        print('O triângulo é ISÓSCELES.')
else:
    print('Os segmentos NÃO formam um triângulo')
