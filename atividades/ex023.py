# PROGRAMA QUE LÊ UM NÚMERO COM 4 DÍGITOS E MOSTRA NA TELA CADA UM DOS DIGITOS SEPARADOS 
print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))

num = str(input('--> Digite um número com quatro digitos: '))

unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]

print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')

print('{:=^30}'.format('| OBRIGADO POR USAR |'))