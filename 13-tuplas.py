#### tuplas

## criando tuplas
gase_nobres = ("Helio", "Neón", "Argón", "Kriptón", "Xenón", "Radón")
print(gase_nobres)

for gases in gase_nobres:
    print(gases)

## convertendo tupla em lista
halogenios = ("Flúor", "Cloro", "Bromo", "Iodo", "Astato")
grupo17 = list(halogenios)
print(f"De tupla para lista: {grupo17}")

## convertendo lista em tupla
alcalinos_terrosos = ["Berílio", "Magnésio", "Cálcio", "Estrôncio", "Bário", "Rádio"]
grupo2 = tuple(alcalinos_terrosos)
print(f"De lista para tupla: {grupo2}")

## conferindo dados na tupla
t1 = (2, 5, 8, 6, 9, 7, 4, 2, 1, 5, 3, 7, 9, 2, 4, 6, 8, 3, 15, 1, 8, 7, 4, 3, 2, 1)
print(f"\n {t1}")
valor = int(input("Digite um valor para saber quantas vezes ele aparece na tupla: "))
print(t1.count(valor)) # contar quantas vezes o valor aparece na tupla

### operações não permitidas em tuplas
# .sort() # ordenar a tupla
# .append() # adicionar um elemento na tupla
# .insert() # inserir um elemento na tupla
# .reverse() # inverter a tupla
# .pop() # remover um elemento da tupla
# .remove() # remover um elemento da tupla
# .clear() # limpar a tupla
# valores[0] = 3 # alterar o valor do primeiro elemento da tupla
