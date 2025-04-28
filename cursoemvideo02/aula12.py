nome = str('Tenha um bom dia')
if nome == 'Felipe':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Leticia' or nome == 'Gustavo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Julia Paula Cleusa':
    print('Ola mulher')

else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format())