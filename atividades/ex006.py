# ALGORITMO QUE MOSTRA O DOBRO, TRIPLO E A RAIZ QUADRADA DE UM NÚMERO

print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))

numero = int(input('--> Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raizquadrada = numero ** (1/2)

print('O dobro do número: {} é = {} \nO triplo do número: {} é = {} \nA raiz quadrada do número: {} é = {:.0f}'.format(numero, dobro, numero, triplo, numero, raizquadrada))

print('{:=^30}'.format('| OBRIGADO POR USAR ! |'))
