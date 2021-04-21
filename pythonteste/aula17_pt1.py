#LISTAS PARTE 1
#estrutura que recebe vários elementos entre colchetes []

num = [2, 5, 9 ,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2) #elimina o primeiro valor 2
#num.pop() #elimina o último elemento
#num.pop(2) #elimina o segundo elemento
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores:
    print(f'{valor}...', end='')
print('\n')

'''valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista\n')'''

a = [2, 3, 4, 7]
#b = a #quando se igualam duas listas, cria-se um vínculo entre elas, o que muda em uma, muda na outra
b = a[:] #cria-se uma cópia dos valores de a e não uma ligação entre as listas
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
