velocidade = float(input('Digite a velocidade do carro'))
multa = (velocidade-80) *7
if velocidade > 80.0:
    print('voce foi multado, e devera pagar {:.2f} reais'.format(multa))
else:
    print('Voce nao foi multado')