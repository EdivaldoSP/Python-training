import time
import math
# # PROGRAMA QUE CALCULA A HIPOTENUSA DE UM TRIÂNGULO RETÂNGULO
print('{:=^30}'.format('| SEJA BEM VINDO (A)|'))

oposto = int(input('--> Digite o comprimento do cateto oposto: '))
adjacente = int(input('--> Digite o comprimento do cateto adjacente: '))

# fórmula: c² = a² + b²

hipotenusa1 = (oposto ** 2) + (adjacente ** 2)

hipotenusa2 = math.isqrt(hipotenusa1)

print('Calculando, aguarde...')

time.sleep(2)

print('O comprimento da hipotenusa é {}.'.format(hipotenusa2))

print('{:=^30}'.format('| OBRIGADO POR USAR |'))

# teste = int(input('Digite numeoro: '))

# print('A raiz de {} é {}'.format(teste, math.sqrt(teste)))