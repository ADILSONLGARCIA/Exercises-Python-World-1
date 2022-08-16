from random import randint
from time import sleep
computador = randint(0, 5)
#meio que faz o computador "pensar"
print('-_-_-_-' * 10)
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
print('-_-_-_-' * 10)
jogador = int(input('Em que número eu pensei?'))
#jogador meio que tenta advinhar
print('Processando ...')
sleep(2)
if jogador == computador:
    print('PARABÉNS você conseguiu advinhar ! ! !')
else:
    print('Voce ERROU ! ! !')
    print('O número que pensei foi {} e o número apontado por você foi {}.'.format(computador, jogador))
    print('Tente de novo ! ! !')
print('-_-_-_-' * 10)



