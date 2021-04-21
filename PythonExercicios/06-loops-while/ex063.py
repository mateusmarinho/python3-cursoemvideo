# n primeiros termos da Sequência de Fibonacci
print('SEQUÊNCIA DE FIBONACCI')
n = int(input('Digite a quantidade de termos: '))
print('~'*30)
ant = 0
atual = 1
print('{} - {}'.format(ant, atual), end='')
while n - 2 > 0:
    fib = ant + atual
    print(' - {}'.format(fib), end='')
    ant = atual
    atual = fib
    n -= 1
print('\nFIM')
