letras = str(input('Entre com uma frase, para podermos analisa-la:  ')).lower().strip()
print('A letra A aparece {} vezes dentro desta frase.'.format(letras.count('a')))
print('A primeira letra A apareceu na posição {}.'.format(letras.find('a')+1))
print('A ultima letra A apareceu na posição {}.'.format(letras.rfind('a')+1))


