# PROGRAMA QUE CALCULA A ÁREA DE UMA PAREDE

print('{:=^38}'.format('| SEJA BEM VINDO (A) ! |'))

altura = float(input('--> Digite a altura da parede: '))
largura = float(input('--> Digite a largura da parede: '))

area = altura * largura

litro = 2

calculo = area / litro

print('A área da parede é de: {} m²'.format(area))
print('Para pintar a parede, vai ser necessário: {} litros'.format(calculo))

print('{:=^38}'.format('| OBRIGADOR POR USAR! |'))
