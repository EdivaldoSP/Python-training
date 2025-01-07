pessoas = {
    'nome': 'Edivaldo',
    'sexo': 'M',
    'idade': 18
}

del pessoas['sexo']

for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []

estado1 = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ',
}
estado2 = {
    'uf': 'São Paulo',
    'sigla': 'SP',
}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)

estado = {

}

brasil = []

for i in range(0, 3):
    estado['uf'] = input("Digite o nome do estado: ")
    estado['sigla'] = input("Digite a sigla do estado: ")
    brasil.append(estado.copy())

for estado in brasil: 
    print(f'{estado['uf']} : {estado['sigla']}')

