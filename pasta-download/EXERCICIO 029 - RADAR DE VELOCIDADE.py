velocidade = float(input('DIGITE A VELOCIDADE DO VEÍCULO:  '))
multa = float((velocidade - 80) * 7)
escedido = float(velocidade - 80)
if velocidade > 80:
    print(
        'Você foi MULTADO, sua velocidade foi {:.2f} KM/H excedendo em {:.2f} KM/H, por isso sua multa será de R$ {:.2f}!'.format(
            velocidade, escedido, multa))
else:
    print('Boa viagem! Dirija com segurança!')
