from datetime import date

atual = date.today().year
nacs = int(input('Ano de Nascimento: '))
idade = atual - nacs

if idade < 18:
    print('Quem nasceu em {} tem {}, portanto nao esta na hora de alistar!'.format(nacs, idade))
elif idade > 18:
    print('Quem nasceu em {} tem {}, portanto ja passou da hora de se alistar!'.format(nacs, idade))
elif idade == 18:
    print('Quem nasceu em {} tem {}, portanto esta na hora de se alistar!'.format(nacs, idade))