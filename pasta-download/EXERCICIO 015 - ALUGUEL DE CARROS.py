dias = int(input('Quantos dias alugado?'))
km = float(input('Quantos kilometros foram rodados?'))
pago = (dias * 60) + (km * 0.25)
print('O total a pagar é de R${:.2f}'.format(pago))
