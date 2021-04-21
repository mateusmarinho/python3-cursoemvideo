'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor
lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: Número fatorial a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial do número
    """
    f = 1
    if show:
        for i in range(num, 0, -1):
            f *= i
            print(i, end='')
            if i != 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    else:
        for i in range(num, 0, -1):
            f *= i
    return f


# programa principal
print(fatorial(5, True))
