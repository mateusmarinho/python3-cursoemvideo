# FUNÇÕES PARTE 2

## função help()

'''help(input)
print(input.__doc__)'''

## docstrings


'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='.. ')
        c += p
    print('FIM!')


contador(0, 10, 1)
help(contador)'''

## parâmetros opcionais


'''def somar(a=0, b=0, c=0):
        s = a + b + c
        print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()'''

## escopo de variáveis


'''def funcao():
    # para utilizar uma variável global dentro da função, declarar a variável acompanhada da palavra "global"
    n1 = 4
    print(f'N1 local vale {n1}')


n1 = 2
funcao()
print(f'N1 global vale {n1}')'''

## retorno de valores (return)


'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')'''

## prática 1: fatorial de um número


'''def fatorial(num=1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f


#n = int(input('Digite um número: '))
#print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2} e {f3}')'''

## prática 2: return com valor lógico


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
