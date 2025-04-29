from uuid import uuid4
from time import sleep


lista = ['Felipe', 'Ana' , 'Manoel', 'Alex', 'Pietra']


print(3* '_______________') 
print('IDENTIFICADOR DE NOMES')
print(3* '_______________') 
sleep (2)

nome = str(input('Digite seu nome para receber seu id para entrar na festa: '))

def identificador():
    if nome in lista :
        print('Este é seu numero de serie {}: {}'.format(nome, uuid4()))
    else:
        print('Seu nome nao esta na nossa lista de convidados, por favor se retire!')

identificador()




