'''Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''


def linha(n):
    print('~' * n)


def escreva(txt):
    tam_linha = len(txt) + 4
    linha(tam_linha)
    print(f'{txt:^{tam_linha}}')
    linha(tam_linha)


# Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
