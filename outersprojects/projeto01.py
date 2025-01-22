import random

print('Seja muito bem vindo ao guess number do Felipe')
choice_number = input('Digite o numero teto do desafio: ')

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print('ERRO, valor informado nao numerico')
    quit()

random_number = random.randint(0, choice_number)

while True:
    answer_user = input('Advinhe um numero: ')

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
         print('ERRO, valor informado nao numerico')
         continue
    
    if answer_user == random_number:
        print('Acertou')
        break
    elif answer_user > random_number:
        print('Chutou alto o numero randomico é menor que isso')
    else:
        print('O numero é maior')


    
        



