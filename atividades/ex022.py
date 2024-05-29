# PROGRAMA QUE LÊ O NOME COMPLETO DE UMA PESSOA 

print('{:=^30}'.format('|  SEJA BEM VINDO(A) |'))

nome = str(input('--> digite o seu nome completo: '))

maiúscula = nome.upper()

minúscula = nome.lower()

dividir = nome.split()
juntar = ''.join(dividir)
contar = len(juntar)

dividir2 = nome.split()
contar2 = len(dividir2[0])

print(f'O nome {nome} com: \nTodas as letras maiúsculas: {maiúscula}\nTodas as letras minúsculas: {minúscula}\nQuantas letras ao todo: {contar}\nQuantas letras tem o primeiro nome: {contar2}')

print('{:=^30}'.format('| OBRIGADO POR USAR |'))