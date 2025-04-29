import math

ang = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno ))

cos = math.cos(math.radians(ang))
print('O angulo de {} tem o cosseno de {:.2f}'.format(ang, cos))

tan = math.tan(math.radians(ang))
print('O angulo de {} tem a tangente de {:.2f}'.format(ang, tan))