peso = float(input('Digite o peso da 1ª pessoa: '))
maior = peso
menor = peso
for i in range(1, 5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i + 1)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso foi {} kg.'.format(maior))
print('O menor peso foi {} kg.'.format(menor))
