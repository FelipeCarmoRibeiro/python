from random import randint

computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um numero entre 0 e 10")
print("Sera que voce consegue descobrir qual o numero")

acertou = False
palpites = 0 
while not acertou:
    jogador = int(input("Digite um numero: "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez")
        elif jogador > computador:
            print("Menos... Tente mais uma vez")
print("Acertou com {} palpites!".format(palpites))