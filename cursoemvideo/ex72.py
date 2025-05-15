n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opçao = 0 
while opçao != 5:
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos numeros
    [5]Sair do Programa
    ''')

    opçao = int(input("Qual é a sua opçao: "))
    if opçao == 1:
        soma = n1 + n2
        print(soma)
    elif opçao == 2:
        soma = n1 * n2
        print(soma)
    
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("O numero maior é {}".format(maior))

    elif opçao == 4:
        print("Informe os numeros novamente:")
        n1 = int(input())
        n2 = int(input())
    elif opçao == 5:
        print("finalizando...")
    
    else:
        print("Opçao invalidada, tente novamente")

print("Fim do programa, Volte sempre")
