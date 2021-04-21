from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    op = int(input('Digite a sua opção: '))
    if op == 1:
        print('Soma: {} + {} = {}'.format(n1, n2, n1+n2))
    elif op == 2:
        print('Produto: {} x {} = {}'.format(n1, n2, n1*n2))
    elif op == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        elif n1 < n2:
            print('O maior número é {}'.format(n2))
        else:
            print('Os números são iguais.')
    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Encerrando...')
    else:
        print('Opção inválida!')
    print('-=-'*10)
    sleep(2)
print('Fim do programa!')
