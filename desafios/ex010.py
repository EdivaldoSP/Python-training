import time
# CONVERTOR DE REAL PARA DÓLAR
print('{:=^38}'.format('| SEJA BEM VINDO (A)! |'))

real = int(input('--> Digite o valor em reais (R$): '))
# considere: US$1.00 = R$3,27
dolar = 3.27

convert = real / dolar

print('Convertendo, aguarde ...')
time.sleep(2)
print('O valor digitado equivale à {:.2f} US$!'.format(convert))

print('{:=^38}'.format('| OBRIGADOR POR USAR |'))
