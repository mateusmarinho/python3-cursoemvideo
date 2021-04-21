#Soma dos ímpares múltiplos de 3 entre 1 e 500
cont = 0
s = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
        cont += 1
print('A soma de todos os {} valores solicitados foi: {}'.format(cont, s))
