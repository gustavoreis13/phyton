d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
s1 = (d * 60) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}.'.format(s1))