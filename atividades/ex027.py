# PROGRAMA QUE LÊ O NOME COMPLETO E MOSTRA O PRIMEIRO E O ÚLTIMO NOME SEPARADO

print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))

nome = str(input('--> Digite seu nome completo: '))

dividir = nome.split()

print('O primeiro nome é: {}'.format(dividir[0]))
print('O último nome é: {}'.format(dividir[-1]))

print('{:=^30}'.format('| OBRIGADO POR USAR |'))