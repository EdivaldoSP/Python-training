import time

# PROGRAMA QUE CALCULA O ALUGUEL DE UM CARRO

print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))

km = float(input('--> Quantos quilômetros percorridos? '))
dias = int(input('--> E quantos dias alugados? '))

calculo1 = km * 0.15
calculo2 = dias * 60

calculo3 = calculo1 + calculo2

print('Calculando, aguarde...')

time.sleep(2)

print('O total a pagar é de R$ {:.2f}'.format(calculo3))

print('{:=^30}'.format('| OBRIGADO POR USAR |'))