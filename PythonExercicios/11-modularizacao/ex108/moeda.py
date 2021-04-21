def aumentar(p=0, taxa=0):
    r = p + (p * taxa / 100)
    return r


def diminuir(p=0, taxa=0):
    r = p - (p * taxa / 100)
    return r


def dobro(p=0):
    return p * 2


def metade(p=0):
    return p / 2


def moeda(p=0, moeda='R$'):
    return f'{moeda} {p:>.2f}'.replace('.', ',')