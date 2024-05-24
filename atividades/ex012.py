# ALGORITMO QUE CALCULA O PREÇO DE UM PRODUTO COM 5% DE DESCONTO
print('{:=^38}'.format('| SEJA BEM VINDO(A)! |'))

produto = float(input('--> Digite o valor do produto em reais: '))

desconto = 5 * produto / 100

produdodesconto = produto - desconto

print('O valor do produto com 5% de desconto é: R$ {}'.format(produdodesconto))

print('{:=^38}'.format('| OBRIGADO POR USAR! |'))