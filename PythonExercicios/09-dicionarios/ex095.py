'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um
sistema de visualização de detalhes do aproveitamento de cada jogador.'''

time = []
jogador = dict()
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    for i in range(0, partidas):
        gols.append(int(input(f'    Quantos gols na partida {i}?: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    while True:
        resp = str(input('Deseja continuar [S/N]?: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda com S ou N.')
    if resp == 'N':
        break
print('-=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for p, v in enumerate(time):
    print(f'{p:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [Digite o cod ou 999 para encerrar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o cod {busca}!')
    else:
        print(f'  --  LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols.')
    print('-' * 40)
