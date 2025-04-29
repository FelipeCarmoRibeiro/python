salario = float(input('Qual o salario do funcionario?: '))
aumento = salario + (salario*15/100)
print('Um funcionario que ganhava {}, com 15% de aumento, passa a receber {:.5f}'.format(salario, aumento))