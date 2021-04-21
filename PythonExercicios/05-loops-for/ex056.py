somaidade = 0
maioridadehomem = 0
mulhersub20 = 0
for i in range(0, 4):
    print('------{}ª PESSOA------'.format(i+1))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    somaidade += idade
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        mulhersub20 += 1
print('Média de idade do grupo: {} anos.'.format(somaidade/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomemaisvelho))
print('No grupo, {} mulheres tem menos de 20 anos.'.format(mulhersub20))
