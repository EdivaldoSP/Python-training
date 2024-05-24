import time
import math

# PROGRAMA QUE MOSTRA O SENO E CONSCENO DE UM DETERMINADO ÂNGULO

print('{:=^30}'.format('| SEJA BEM VIDO (A) |'))

angulo = int(input('--> Digite o ângulo: '))

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('Calculando, aguarde...')

time.sleep(2)

print('Dado o ângulo {}, o seno é: {:.2f}, o cosseno é: {:.2f} e a tangente é: {:.2f}'.format(angulo, seno, cosseno, tangente))

print('{:=^30}'.format('| OBRIGADO POR USAR |'))