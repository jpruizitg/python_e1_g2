# listas continuación

# Ej.12 - método append()
numeros = [123, 45, 23, 12]

print('lista original:', numeros)
print('longitud lista original:', len(numeros))

numeros.append(1000)

print('lista nueva:', numeros)
print('longitud lista nueva:', len(numeros))

print()

# Ej.13 - seguimos con append()
listaLetras = ['uno', "dos"]
print(listaLetras)

listaLetras.append('tres')
print(listaLetras)

print()

# Ej.14 - método insert()
transportes = ['auto', 'moto', 'barco']
print('original:', transportes)

transportes.insert(2, 'tren')
print('nueva', transportes)

print()

# Ej.15 - método insert()
newLista = [49, 23, 65, 87]
print('original:', newLista)

newLista.insert(-2, 1000)
print('nueva:', newLista)

print()

# Ej.15 - agregando elementos a una lista vacía
my_list = []

for i in range(5):
    my_list.append(i + 1)

print('lista nueva:', my_list)

print()

# Ej.17 - lista vacía cargar elementos con insert()
my_list2 = []

for i in range(5):
    my_list2.insert(0, i + 1)
    
print('nueva:', my_list2)
