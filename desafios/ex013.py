import time
# ALGORITMO QUE CALCULA 15% DE UM SALÁRIO E SOMA
print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))

salario = float(input('--> Digite o valor do salário: '))

salario_com_porcentagem = (15 * salario) / 100

salario_liquido = salario + salario_com_porcentagem

print(f'15% do salário equivale à: R$ {salario_com_porcentagem}')

time.sleep(2)

print(f'O novo salário do funcionário com 15% de aumento é de: R$ {salario_liquido}')

print('{:=^30}'.format('| OBRIGADO POR USAR |'))


