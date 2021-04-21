'''co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa é {:.3f}'.format(h))'''
'''from math import sqrt, pow
co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
h = sqrt(pow(co, 2) + pow(ca, 2))
print('O valor da hipotenusa é {:.3f}'.format(h))'''
import math
co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
h = math.hypot(co, ca)
print('O valor da hipotenusa é {:.3f}'.format(h))
