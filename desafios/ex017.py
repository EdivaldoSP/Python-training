import time
import math
# # PROGRAMA QUE CALCULA A HIPOTENUSA DE UM TRIÂNGULO RETÂNGULO

# CALCULANDO SEM USAR A BIBLIOTECA MATH 👇

print('{:=^30}'.format('| SEJA BEM VINDO (A)|'))

oposto = float(input('--> Digite o comprimento do cateto oposto: '))
adjacente = float(input('--> Digite o comprimento do cateto adjacente: '))

# fórmula: c² = a² + b²

hipotenusa1 = (oposto ** 2 + adjacente ** 2) ** (1/2)

print('Calculando, aguarde...')

time.sleep(2)

print('O comprimento da hipotenusa é {:.2f}.'.format(hipotenusa1))

print('{:=^30}'.format('| OBRIGADO POR USAR |'))

# CALCULANDO USANDO A BIBLIOTECA MATH

print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))

aposto= float(input('--> Digite o comprimento do cateto oposto: '))
adjacente = float(input('--> Digite o comprimento do cateto adjacente: '))

hipotenusa = math.hypot(aposto, adjacente)

print('Calculando, aguarde...')

time.sleep(2)

print('O comprimento da hipotenusa é {:.2f}.'.format(hipotenusa))

print('{:=^30}'.format('| OBRIGADO POR USAR |'))