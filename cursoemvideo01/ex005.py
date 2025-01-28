dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos kms ele rodou: '))
pago = (dias*60) + (km*0.15)
print('O total de a pagar é {:.2f}'.format(pago))

