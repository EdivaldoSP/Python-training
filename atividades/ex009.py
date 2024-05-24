import time
# PROGRAMA QUE MOSTRA A TABUADA DE UM NÚMERO DIGITADO PELO USUÁRIO

print('{:=^30}'.format(' |SEJA BEM VINDO (A)|'))
n = int(input('--> Digite um número positivo: '))

print('Ok, o número digitado foi: {}'.format(n))

print('Gerando tabuada [...]')
time.sleep(2)

print('-' * 30)

casa0 = n * 0
casa1 = n * 1
casa2 = n * 2
casa3 = n * 3
casa4 = n * 4
casa5 = n * 5
casa6 = n * 6
casa7 = n * 7
casa8 = n * 8
casa9 = n * 9
casa10 = n * 10

print('|------   {} x 0 = {}    ------| \n|----     {} x 1 = {}      ----| \n|------   {} x 2 = {}    ------| \n|----     {} x 3 = {}      ----| \n|------   {} x 4 = {}    ------| \n|----     {} x 5 = {}     ----| \n|------   {} x 6 = {}   ------| \n|----     {} x 7 = {}     ----| \n|------   {} x 8 = {}   ------| \n|----     {} x 9 = {}     ----| \n|------   {} x 10 = {}  ------|'.format(n, casa0, n, casa1, n, casa2, n, casa3, n, casa4, n, casa5, n, casa6, n, casa7, n, casa8, n, casa9, n, casa10))
print('-' * 30)

print('{:=^30}'.format('| OBRIGADOR POR USAR |'))



