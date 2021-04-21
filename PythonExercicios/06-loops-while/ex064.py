n = int(input('Digite um número: '))
soma = 0
cont = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
print('Foram digitados {} números. A soma dos valores digitados foi {}.'.format(cont, soma))
