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


def resumo(p=0, taxa_a=10, taxa_r=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{taxa_a}% de aumento: \t{aumentar(p, taxa_a, True)}')
    print(f'{taxa_r}% de redução: \t{diminuir(p, taxa_r, True)}')
    print('-' * 30)

