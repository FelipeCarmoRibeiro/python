valor_casa = int(input('Digite o valor da casa: '))
salario = int(input('Qual seu salario: '))
anos_de_financiamento = int(input('Quantos anos deseja finaciar a casa?: '))

prestaçao = valor_casa / anos_de_financiamento 

print('Para pagar uma casa de {} em {} anos a prestaçao sera {}'.format(valor_casa, anos_de_financiamento,prestaçao ))

if salario < (10/100) * valor_casa:
    print('Financiamento negado!')
else:
    print('Financiamento aceito')
