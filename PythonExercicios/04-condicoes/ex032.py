from datetime import date
ano = int(input('Que ano deseja analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano BISSEXTO!'.format(ano))
else:
    print('{} NÃO é um ano BISSEXTO!'.format(ano))
