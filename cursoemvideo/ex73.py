from math import factorial


num = int(input("Digite um numero, para calcular seu fatorial: "))
f =  1
c = num
print("Calculando {}! = ".format(num), end="")
while c > 0:
    print("{}".format(c), end="")
    print(" x " if c > 1 else "=", end="")
c = c -1

#print("O fatorial de {} é {}".format(num, f))

#nao consegui fazer esse exercicio

