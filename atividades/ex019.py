import random
import time

# PROGRAMA QUE SORTEIA O NOME DOS ALUNOS

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

aleatorio = random.choice(alunos)

print('sorteando, aguarde...')

time.sleep(2)

print('O aluno escolhido foi: {}'.format(aleatorio))

print('{:=^30}'.format('| OBRIGADO POR USAR |'))