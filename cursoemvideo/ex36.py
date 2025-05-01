valor_casa = float(input('Digite o valor do carro: R$: '))
salario = float(input('Qual seu salario: R$: '))
anos_de_financiamento = int(input('Quantos anos deseja finaciar o carro?: R$: '))

prestaçao = valor_casa /  (anos_de_financiamento *12) 
minimo = salario  * 30 / 100 

print('Para pagar uma casa de {:.2f} em {} anos a prestaçao sera {:1.3f}'.format(valor_casa, anos_de_financiamento,prestaçao ))

if prestaçao > minimo:
    print('Financiamento negado!')
else:
    print('Financiamento aceito')
    