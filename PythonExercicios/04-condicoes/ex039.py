from datetime import date
nasc = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade < 18:
    print('Você deverá se alistar ao serviço militar em {} anos.'.format(18 - idade))
    print('Seu ano de alistamento será {}.'.format(nasc + 18))
elif idade > 18:
    print('Já passou/passaram {} ano(s) do seu alistamento.'.format(idade - 18))
    print('Seu ano de alistamento foi {}.'.format(nasc + 18))
else:
    print('Está na hora de se alistar!')
