'''cidade = input('Digite o nome de uma cidade: ').strip().capitalize().split()
print('Santo' in cidade[0])'''
cidade = input('Digite o nome de uma cidade: ').strip()
print(cidade[:5].upper() == 'SANTO')
