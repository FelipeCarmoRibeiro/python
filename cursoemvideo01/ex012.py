import time

num = int(input('Informe um numero: '))
n = str(num)
print('Analisando 0 numero {}'.format(num))
time.sleep(2)
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}' .format(n[1]))
print('Milhar: {}' .format(n[0]))