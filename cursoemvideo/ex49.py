peso = int(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Voce esta abaixo do peso normal')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Voce esta com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Voce esta obeso')
else:
    print('Obesidade morbida')