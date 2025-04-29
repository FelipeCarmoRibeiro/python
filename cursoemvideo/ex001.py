larg = float(input('Largura da parede: '))
height = float(input('Altura da parede: '))
area = larg * height
print('Sua parede tem a dimensao de {}x{} e a sua area é de {}m2' .format(larg, height, area))
tinta = area/ 2
print('Para pintar essa area precisa de {} litros de tinta'.format(tinta))