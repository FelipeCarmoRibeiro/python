nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
nt3 = float(input('Digite a terceira nota: '))

media = (nt1 + nt2 + nt3) / 3

print('Tirando: {:.1f}, {:.1f}, {:.1f}, a media do aluno é {:.1f}'.format(nt1, nt2, nt3, media))
print(media)

if media >=5 and media < 7:
    print('O aluno esta em recuperaçao')
elif media < 5:
    print('O aluno esta reprovado')
else:
    print('O aluno esta aprovado')

