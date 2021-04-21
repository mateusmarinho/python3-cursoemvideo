'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = dict()
catalogo = list()
while True:
    dados['nome'] = str(input('Digite o nome: ')).strip()
    while True:
        dados['sexo'] = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas com M ou F.')
    dados['idade'] = int(input('Digite a idade: '))
    catalogo.append(dados.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]?: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'Nn':
        break
print(catalogo)
print('-=' * 40)
print(f'Pessoas cadastradas: {len(catalogo)}')
somaIdade = 0
mulheres = list()
for pessoa in catalogo:
    somaIdade += pessoa['idade']
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa['nome'])
mediaIdade = somaIdade / len(catalogo)
print(f'Média de idade: {mediaIdade} anos')
print(f'Mulheres cadastradas: {mulheres}')
print(f'Pessoas com idade acima da média: ')
for pessoa in catalogo:
    if pessoa['idade'] > mediaIdade:
        print('    ', end='')
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO!>>')
