import time
import math

# PROGRAMA QUE MOSTRA O SENO E CONSCENO DE UM DETERMINADO ÂNGULO

print('{:=^30}'.format('| SEJA BEM VIDO (A) |'))

angulo = float(input('--> Digite o ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Calculando, aguarde...')

time.sleep(2)

print('Dado o ângulo {}, o SENO é: {:.2f}, o COSSENO é: {:.2f} e a TANGENTE é: {:.2f}'.format(angulo, seno, cosseno, tangente))

print('{:=^30}'.format('| OBRIGADO POR USAR |'))