maiorde18 = homens = mulheres20 = 0
while True:
    print('-='*20)
    print('NOVO CADASTRO')
    print('-='*20)
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()[0]
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = input('Você deseja continuar? [S/N]: ').strip().upper()[0]
    if idade > 18:
        maiorde18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    if resposta == 'N':
        break
print('-'*30)
print(f'Pessoas com mais de 18 anos: {maiorde18}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheres20}')