d =float(input('Quantos dias o carro foi alugado?'))
dp = d * 60
k =float(input('Quantos km foram rodados ?'))
kp = k * 0.15
pt = dp + kp
print('-' * 15)
print('O valor do aluguel do carro é R${}'.format(pt))
print('-' * 15)