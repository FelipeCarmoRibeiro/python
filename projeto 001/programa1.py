from uuid import uuid4
from time import sleep


nome = ['Felipe', 'Ana' , 'Manoel', 'Alex', 'Pietra']

print(15* '_______________') 
print('IDENTIFICADOR DE NOMES')
print(15* '_______________') 
sleep (2)

input('Digite seu nome para receber seu id para entrar na festa: ')

def identificador():
    if nome in nome:
        print('Este é seu numero de serie {}: {}'.format(nome, uuid4()))
    else:
        print('Seu nome nao esta na nossa lista de convidados, por favor se retire!')

identificador()




