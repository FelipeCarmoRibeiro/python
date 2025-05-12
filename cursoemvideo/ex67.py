soma_idade = 0
media = 0
maior_idade = 0 
nome_velho = ""
totmulher = 0
for c in range(1, 5):
    print("{}pessoa".format(c))
    n = str(input("Nome: ")).strip()
    i = int(input("Idade: "))
    s = str(input("Sexo[M/F]: ").strip())
    soma_idade += i
    if c == 1 and s in "Mm":
        maior_idade = i
        nome_velho = n
    if s in "Mm" and i > maior_idade:
        maior_idade = i
        nome_velho = n
    if s in "Ff" and i <20:
        totmulher += 1


media = soma_idade /4
print("A idade media de todos sao {}".format(media))
print("O homem mais velho tem {} e se chama".format(maior_idade, nome_velho))
print("Ao todo sao {} mulheres com menos de 20 anos".format(totmulher))

