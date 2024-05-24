import math
import time
# PROGRAMA QUE LÊ UM NÚMERO REAL E MOSTRA SUA POSIÇÃO INTEIRA NA TELA
print('{:=^30}'.format("| SEJA BEM VINDO (A) |"))

num = float(input('--> Digite um número real \n(Exemplo: 1.98632... etc): '))
inteira = math.floor(num)

print('Calculando, aguarde...')

time.sleep(2)

print('O número {} tem a parte inteira {}.'.format(num, inteira))

print('{:=^30}'.format('| OBRIGADO POR USAR |'))
