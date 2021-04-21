frase = 'Curso em Vídeo Python'

'''Fatiamento'''
#print(frase)
#print(frase[3])
#print(frase[3:13])
#print(frase[:13])
#print(frase[13:])
#print(frase[1:15])
#print(frase[1:15:2])
#print(frase[1::2])
#print(frase[::2])

'''Análise'''
#print(len(frase))
#print(frase.count('o'))
#print(frase.count('o', 0, 13))
#print(frase.upper().count('O'))
#print('Curso' in frase)
#print(frase.find('Curso'))
#print(frase.find('Vídeo'))
#print(frase.find('video'))

'''Transformação'''
#frase = '   Curso em Video Python  '
#print(len(frase.strip()))
#print(frase.replace('Python', 'Android'))
#print(frase.lower().find('vídeo'))
#print(frase.split())
div = frase.split()
print(div[0])
print(div[2][3])
