num = int(input('Digite um número: '))
tot = 0
for cont in range(1, num+1):
    if num % cont == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[37m', end=' ')
    print('{}'.format(cont), end=' ')
print('\n\033[mO número foi divisível {} vezes.'.format(tot))
if tot > 2:
    print('O número {} NÃO é PRIMO.'.format(num))
else:
    print('O número {} É PRIMO.'.format(num))
