from random import randint
from time import sleep
computer = randint(0, 100)
jogador = int(input('Digite um numero: '))
print('Vou pensar em um numero')
print('O numero que pensei foi {}'.format(computer))

sleep(2)
if jogador == computer:
    print('Acertou mizeravi')
else:
    print('Erro mizeravi')