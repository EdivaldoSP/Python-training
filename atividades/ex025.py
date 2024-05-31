# PROGRAMA QUE LÊ UM NOME DE UMA PESSOA E DIZ SE APARECE "SILVA" NELE

print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))

nome = str(input('--> Digite seu nome completo: '))

procurar1 = 'SILVA' in nome
procurar2 = 'Silva' in nome
procurar3 = 'silva' in nome

if procurar1 == False and procurar2 == False and procurar3 == False:
    print('No seu nome não aparece "SILVA".')
elif procurar1 == True and procurar2 == False and procurar3 == False:
    print('No seu nome aparece "SILVA".')
elif procurar1 == False and procurar2 == True and procurar3 == False:
    print('No seu nome aparece "SILVA".')
elif procurar1 == False and procurar2 == False and procurar3 == True:
    print('No seu nome aparece "SILVA".')      

print('{:=^30}'.format('| OBRIGADO POR USAR  |'))