import random
import time

# PROGRAMA QUE SORTEIA A ORDEM DE APRESENTAÇÃO DOS ALUNOS

print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))

alunos = []

print('Digite os nomes dos alunos abaixo.')

print('-' * 30)


aluno1 = str(input('--> Digite o primeiro nome: '))
aluno2 = str(input('--> Digite o segundo nome: '))
aluno3 = str(input('--> DIgite o terceiro nome: '))
aluno4 = str(input('--> Digite o quarto nome: '))

alunos.append(aluno1)
alunos.append(aluno2)
alunos.append(aluno3)
alunos.append(aluno4)

random.shuffle(alunos)

print('sorteando, aguarde...')

time.sleep(2)

print(f'Os aluno escolhidos foram: 1° {alunos[3]}, 2° {alunos[2]}, 3° {alunos[1]}, 4° {alunos[0]}.')

print('{:=^30}'.format('| OBRIGADO POR USAR |'))