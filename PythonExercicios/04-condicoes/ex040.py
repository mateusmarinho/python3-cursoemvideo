n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
print('Média: {:.1f}'.format(media))
if media < 5.0:
    print('Aluno reprovado!')
elif 7.0 > media >= 5.0:
    print('Aluno em recuperação!')
else:
    print('Aluno aprovado!')
