#### dicionario

elemento = {
    'numero': 3,
    'nome': 'Lítio',
    'simbolo': 'Li',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

# print(f'Elemento: {elemento['nome']}')
# print(f'Simbolo: {elemento['simbolo']}')
# print(f'Número: {elemento['numero']}')
# print(f'Grupo: {elemento['grupo']}')
# print(f'Densidade: {elemento['densidade']}')
# print(f'O dicionario possui {len(elemento)} elementos')

# ## # atualizar uma entrada
# elemento['grupo'] = 'Alcalinos'
# print(elemento)

# ## # adicionar uma entrada
# elemento['periodo'] = 1
# print(elemento)

# ## # exclusão de itens 
# del elemento['periodo']
# print(elemento)

# ## todos os itens
# elemento.clear()
# print(elemento)

# ## apagar o dicionario
# del elemento
# print(elemento)

## # visualizando os itens
print(elemento.items())
for i in elemento.items():
    print(i)

## chaves
print(elemento.keys())
for i in elemento.keys():
    print(i)

## valores
print(elemento.values())
for i in elemento.values():
    print(i)

## todos os itens organizados
for i, j in elemento.items():
    print(f'{i}: {j}')

