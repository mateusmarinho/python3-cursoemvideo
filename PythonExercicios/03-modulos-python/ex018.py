from math import sin, cos, tan, radians
a = float(input('Digite o valor do ângulo (graus): '))
a = radians(a)
print('Seno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}'.format(sin(a), cos(a), tan(a)))
