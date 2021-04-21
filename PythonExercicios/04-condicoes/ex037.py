num = int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão:
[1] converte para BINÁRIO
[2] converte para OCTAL
[3] converte para HEXADECIMAL''')
op = int(input('Digite a sua opção: '))
if op == 1:
    print('Em binário: {} = {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('Em octal: {} = {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('Em hexadecimal: {} = {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
