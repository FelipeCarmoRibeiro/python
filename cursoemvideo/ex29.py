distancia = float(input('Distancia da viagem: '))
if distancia < 200.0:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O preço sera {:.2f}'.format(preço))