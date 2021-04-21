#TUPLAS

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') #a sintaxe é a mesma sem os parênteses

print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])

#Tuplas são IMUTÁVEIS
#lanche[1] = 'Refrigerante'

for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba!!')

print(len(lanche))

for count in range(len(lanche)):
    #print(count)
    print(lanche[count])

for pos, comida in enumerate(lanche):
    print(f'Opção {pos} - Eu vou comer {comida}')

#imprime em ordem
print(sorted(lanche))

#mudando o exemplo
a = (2, 5, 4)
b = (5, 8, 1, 2)

print(a)
print(b)

c = a + b

print(c)

d = b + a

print(d)

#alguns métodos da tupla
print(c.count(5)) #conta a ocorreância de um item
print(c.index(8)) #mostra a posição de um item

#próximo exemplo
pessoa = ('Gustavo', 39, 'M', 99.88) #as tuplas podem ter dados de tipos diferentes
print(pessoa)

del(pessoa) #apaga a tupla inteira