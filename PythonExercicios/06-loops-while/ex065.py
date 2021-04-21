resp = 'S'
soma = 0
cont = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = input('Quer continuar [S/N]?: ').strip().upper()[0]
media = soma / cont
print('Você digitou {} números. A média foi: {}'.format(cont, media))
print('O maior número foi {}. O menor número foi {}.'.format(maior, menor))
