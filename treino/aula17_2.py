# teste = list()
# teste.append("Gustavo")
# teste.append(40)
# galera = list()
# galera.append(teste[:])

# teste[0] = "Edivaldo"
# teste[1] = 18
# galera.append(teste[:])
# print(galera)

# galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]

# print(galera[1][0])

galera = list()
dado = list() # lista temporaria

for i in range(4):
    dado.append(input("Digite o nome da pessoa: "))
    dado.append(int(input("Digite a idade: ")))
    galera.append(dado[:]) # adiciona a cópia da lista temporária à galera
    dado.clear() # limpa a lista temporária

for p in galera: 
    print(f'{p[0]} tem {p[1]} anos de idade.')

# print(galera)