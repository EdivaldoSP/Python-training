import time
# PROGRAMA QUE CALCULA O ANTECESSOOR E SUCESSOR

print('{:=^30}'.format('| ANTECESSOR & SUCESSOR |'))
numero = int(input("--> Digite um número: "))

ant = numero - 1
suce = numero + 1

time.sleep(1)
print('O antecessor do número: {} é : {}'.format(numero, ant))
time.sleep(1)
print('O sucessor do número: {} é : {}'.format(numero, suce))

print('{:=^30}'.format('| OBRIGADO POR USAR ! |'))
