from datetime import date
maior = 0
menor = 0
atual = date.today().year
for i in range(0, 7):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(i+1)))
    if atual - ano < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo, tivemos:\n{} pessoas maiores de idade.\n{} pessoas menores de idade.'.format(maior, menor))
