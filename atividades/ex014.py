import time
# PROGRAMA QUE FAZ A CONVERSAÇÃO DE GRAUS CELCIUS PARA FAHRENHEIT
print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))

celsius = float(input('--> Digite a temperatura em grau Celsius: '))

conversao = ((celsius * 9) / 5) + 32

print('Calculando, aguarde...')

time.sleep(2)

print('A temperatura em Celsius {:.1f} °C equivale à {:.1f}°F em Fahrenheit!'.format(celsius, conversao))

print('{:=^30}'.format('| OBRIGADO POR USAR |'))