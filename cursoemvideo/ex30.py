from datetime import date

ano = int(input('Digite um ano ai, coloque 0 para ver o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and 100 != 0 or ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Ano nao bissexto')