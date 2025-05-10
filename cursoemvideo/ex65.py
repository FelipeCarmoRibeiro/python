from datetime import date


atual = date.today().year
totmaior = 0 
totmenor = 0


for c in range(1, 8):
    nasc =  int(input("Em que ano a {} pessoa nasceu: ".format(c)))
    idade = atual - nasc
    print("Essa pessoa tem {}".format(idade))
    if idade <=18:
        totmaior += 1
    else:
        totmenor +=1
print("Tem {} pessoas de maior e {} de menor".format(totmaior, totmenor))