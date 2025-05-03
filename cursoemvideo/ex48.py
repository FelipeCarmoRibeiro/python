from datetime import date



nasc =  date.today().year
anasc = int(input('Ano de nascimento: '))
idade = nasc - anasc

print('O atleta tem {} anos.'.format(idade))

if idade < 9:
    print('Classificaçao: Mirim')
elif idade < 14:
    print('Classificaçao: Infatil')
elif idade < 19:
    print('Classificaçao: Junior')
elif idade < 25:
    print('Classificaçao: Senior')
else:
    print('Classificaçao: Master')

