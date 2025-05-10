soma = 0 
cont = 0 
for c in range(0, 7):
    n = int(input("Digite um numero: ").format(c))
    if n % 2 ==0:
        soma = soma + n
        cont = cont +1

print("Voce informou {} numeros e a soma foi {}".format(cont, soma))

