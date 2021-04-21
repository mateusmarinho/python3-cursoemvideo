def aumentar(p=0, taxa=0, formato=False):
    r = p + (p * taxa / 100)
    return r if formato is False else moeda(r)


def diminuir(p=0, taxa=0, formato=False):
    r = p - (p * taxa / 100)
    return r if formato is False else moeda(r)


def dobro(p=0, formato=False):
    r = p * 2
    return r if not formato else moeda(r)


def metade(p=0, formato=False):
    r = p / 2
    return r if not formato else moeda(r)


def moeda(p=0.0, moeda='R$'):
    return f'{moeda} {p:>.2f}'.replace('.', ',')