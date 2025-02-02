
def verificaçao(nome):
    if nome == 'Felipe do Carmo Ribeiro':
       return True
    else:
       return False

nome_do_cliente = input('Digite seu nome: ')

if verificaçao (nome_do_cliente):
   print('Correto')
else:
   print('Incorreto')
