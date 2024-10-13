# # PROGRAMA QUE LÊ UMA FRASE E MOSTRA:
# # 1. Quantas vezes aparece a letra "A".
# # 2. Em que posição ela aparece na primeira vez.
# # 3. Em que posição ela aparece na última vez.

print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))
frase = str(input('--> Digite qualquer frase: ')).upper().strip()

contagem = frase.count('A')
procurar = frase.find('A') + 1
procurar1 = frase.rfind('A') + 1

print('Aparece {} vezes a letra "A" na frase.'.format(contagem))
print('Na primeira vez a letra "A" aparece na posição {}.'.format(procurar))
print('Na última vez a letra "A" aparece na posição {}'.format(procurar1))

print('{:=^30}'.format('| OBRIGADO POR USAR |'))