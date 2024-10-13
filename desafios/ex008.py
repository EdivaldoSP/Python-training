# PROGRAMA QUE FAZ A CONVERSÃO DE METROS P/ CENTIMETROS E MILIMETROS
print('{:=^30}'.format('| CONVERTOR DE MEDIDA |'))
medida = int(input('--> Digite o valor em metros (M): '))

convertcent = medida * 100
convertmeli = medida * 1000
convertkilo = (medida * 10) / 10000

print('O valor em metros: {:.0f}, equivale à {:.0f} centímetros. \nO valor em metros: {:.0f}, equivale à {:.0f} milímetros. \nO valor em metros: {:.0f}, equivale à {} quilômetros.'.format(medida, convertcent, medida, convertmeli, medida, convertkilo))

print('{:=^30}'.format('| OBRIGADO POR USAR! |'))
