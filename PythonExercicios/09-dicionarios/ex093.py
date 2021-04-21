'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols
feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total
de gols feitos durante o campeonato.'''

jogador = dict()
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for i in range(0, partidas):
    gols.append(int(input(f'    Quantos gols na partida {i}?: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 40)
print(jogador)
print('-=' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 40)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for p, v in enumerate(jogador['gols']):
    print(f'    => Na partida {p}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

