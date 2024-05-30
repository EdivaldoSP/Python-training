# PROGRAMA QUE LÊ O NOME DA CIDADE E MOSTRA SE ELA COMEÇA COM 'SANTO' 'Santo' 'santo'
print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))

cidade = str(input('--> Digite o nome da cidade: '))

procurar1 = cidade.find('SANTO')
procurar2 = cidade.find('Santo')
procurar3 = cidade.find('santo')


if procurar1 and procurar2 and procurar3 == -1:
    print('O nome da cidade não começa com "SANTO".')
elif procurar1 == 0 and procurar2 == -1 and procurar3 == -1:
    print('O nome da cidade começa com "SANTO".')
elif procurar1 == -1 and procurar2 == 0 and procurar3 == -1:
    print('O nome da cidade começa com "Santo".')
elif procurar1 == -1 and procurar2 == -1 and procurar3 == 0:
    print('O nome da cidade começa com "santo".')

print('{:=^30}'.format('| OBRIGADO POR USAR |'))
