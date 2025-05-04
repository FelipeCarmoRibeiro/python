from random import randint
from time import sleep


itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)


print('''Suas opçoes
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')

print('-='*11)
jogador = int(input('Qual é a sua jogada? '))
print('-='*11)

print('JO')
sleep(0.3)
print('KEN')
sleep(0.3)
print('PO')
sleep(0.5)

print('O computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[computador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
         print('JOGADOR PERDEU')
    
    else:
        print('Jogada invalida')

elif computador == 1:
        if jogador == 0:
                print('Computador vence')
        elif jogador == 1:
                print('Empate')

        elif jogador == 2:
                print('Jogador venceu')
            
        else:
                print('Jogada invalida')
elif computador == 2:
        if jogador == 0:
            print('Jogador venceu')

        elif jogador == 1:
            print('Computador venceu')
            
        elif jogador == 2:
                print('Empate')
        else:
                print('Jogada invalida')
