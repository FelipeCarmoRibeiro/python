print('Bem vindo ao meu quiz!')
answer_user = input('Quer começar? (S/N)')
print(answer_user)

if answer_user != 'S':
    quit()

score = 0

print ('Começando...')
print('Quem desenvolveu o GTA \n (A)Rockstar Games \n (B)Ubisoft \n (C) CD Project Red \n')
answer_1 = input('Resposta: ')

if answer_1 == 'A':
    print('Correto!!')
    score = score + 1
else:
    print('Incorreto')

print ('Qual é o nome do protagonista de GTA San Andreas \n (A)Carl Jonhson \n (B)Carl Pinto \n (C) Carl Ferreira')
answer_2 = input('Resposta: ')

if answer_2 == 'A':
    print('Correto!!')
    score = score + 1
else:
    print('Incorreto!!')

print(f'Quiz Acabou...Pontuaçao: {score}/2')


