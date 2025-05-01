n = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversao: \n [1]Binario \n [2]Octal \n [3]Hexadecimal') 

opçao = int(input('Qual sua opçao: '))

if opçao == 1:
    print('{} convertido para binario é {}'.format(n, bin(n)))
elif opçao == 2:
    print('{} convertido para octal é {}'.format(n, oct(n)))
elif opçao == 3:
    print('{} convertido para hexadecimal é {}'.format(n, hex(n)))
else:
    print('Opçao invalida. Tente novamente!')
 