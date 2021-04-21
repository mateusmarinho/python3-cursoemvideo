'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
possibilidade da digitação de um número de tipo inválido. Aproveite e crie também
uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        else:
            return n


## Programa principal

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o valor real foi {real}.')