distancia = float(input('Digite aqui a quantidade de kilometros a serem rodados:'))
print('A distancia total da viagem será {} Km, correto?'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O PREÇO da passagem será de R${:.2f}'.format(preço))
