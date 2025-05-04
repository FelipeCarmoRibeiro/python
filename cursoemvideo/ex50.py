print('{:=^40}'.format(' Lojas Ribeiro '))
preço = float(input('Preço das compras: R$ '))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartao
[ 3 ] 2 x no cartao
[ 4 ] 3 x ou mais no cartao            
''')

opçao = int(input('Qual é opçao? '))

if opçao == 1:
    total = preço - (preço *10 /100)
elif opçao == 2:
    total = preço - (preço *5 /100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))


elif opçao == 4:
    total = preço + (preço *20 /100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(total, parcela))

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))