from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('Categoria MIRIM.')
elif idade <= 14:
    print('Categoria INFANTIL.')
elif idade <= 19:
    print('Categoria JUNIOR.')
elif idade <= 25:
    print('Categoria SENIOR.')
else:
    print('Categoria MASTER.')
