# PROGRAMA QUE CALCULA A MÉDIA DE NOTAS
print('{:=^30}'.format('| CALCULAR MÉDIA |'))

n1 = int(input('-> Digite a primeira nota: '))
n2 = int(input('-> Digite a segunda nota: '))
n3 = int(input('-> Digite a terceira nota: '))
n4 = int(input('-> Digite a quarta nota: '))

media = (n1 + n2 + n3 + n4) / 4

print('A média das notas é: {}'.format(media))
print('{:=^30}'.format(' OBRIGADO POR USAR! '))
