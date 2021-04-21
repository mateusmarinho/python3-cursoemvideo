'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.'''
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar [S/N]?: ')).strip()
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opcao = int(input('Mostrar notas de qual aluno? (Digite o No. / 999 para interromper): '))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    elif 0 <= opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]}: {ficha[opcao][1]}')
    else:
        print('OPÇÃO INVÁLIDA!')
