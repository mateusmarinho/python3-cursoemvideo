# import math
from math import sqrt, ceil, floor
import emoji
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}.'.format(num, raiz))
print('A raiz de {} é igual a {:.3f}.'.format(num, raiz))
print('A raiz de {} é igual a {}.'.format(num, ceil(raiz)))
print('A raiz de {} é igual a {}.'.format(num, floor(raiz)))
print(emoji.emojize('Olá, Mundo :earth_americas:', use_aliases=True))
