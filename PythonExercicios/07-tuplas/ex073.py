'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

classifBrasileirao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'Lista de times do Brasileirão: {classifBrasileirao}')
print(f'Os 5 primeiros são: {classifBrasileirao[0:5]}')
print(f'Os 4 últimos são: {classifBrasileirao[-4:]}')
print(f'Times em ordem alfabética: {sorted(classifBrasileirao)}')
posicao = classifBrasileirao.index('Chapecoense') + 1
print(f'A Chapecoense está na {posicao}ª posição.')