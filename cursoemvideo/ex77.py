
soma = 0
cont = 0

while True:
    num = int(input("Digite um numero (999 para parar): "))
    if num == 999:
        break
    cont += 1
    soma += num
print("A soma dos {} numeros foi {}".format(soma, cont))