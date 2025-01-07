num = [2, 5, 9, 1]
num.append(6) 
# num.sort()
num.pop()
if 3 in num:
    num.remove(3)
else:
    print("O número 3 não está na lista.")
print(num)
print(f"Essa lista tem {len(num)} elementos.")

valores = []

valores.append(5)
valores.append(9)
valores.append(4)

for i in valores:
    print(f'{i}', end=' | ') 

for indice, valores in enumerate(valores):
    print(f"Na posição {indice}, encontrei o valor {valores}")
print("Cheguei ao final da lista.")

for i in range(0, 5):
    num = int(input("Digite um valor: "))
    valores.append(num)
print(valores)

A = [2, 3, 4, 7]
B = A[:]

B[2] = 8

print(f"Lista A: {A}")
print(f"Lista B: {B}")

