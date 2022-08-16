larg = float(input('Largura da parede em metros:'))
alt = float(input('Altura da parede em metros:'))
area = larg * alt
print('Sua parede tem a dimensão de {} metros X {} metros e sua área é de {} metros quadrados.'.format(larg, alt, area))
tinta = area /2
print('Para pintar essa parede, você precisará de {} litros de tinta.'.format(tinta))

