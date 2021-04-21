sexo = input('Digite o seu sexo (M/F): ').strip().upper()[0]
while sexo not in 'MF':
    print('Você digitou uma opção inválida!')
    sexo = input('Digite o seu sexo (M/F): ').strip().upper()[0]
print('Sexo: {}'.format(sexo))
