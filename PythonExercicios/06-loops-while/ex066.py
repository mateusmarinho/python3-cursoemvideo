soma = quant = 0
while True:
    n = int(input('Digite um número [digite 999 para parar]: '))
    if n == 999:
        break
    soma += n
    quant += 1
print(f'Foram digitados {quant} números e a soma foi {soma}.')
