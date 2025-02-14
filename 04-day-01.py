# listas en acción (parentesís)

print('Ej.1 - intercambio de valores')

variable1 = 1
variable2 = 2

variable2 = variable1
variable1 = variable2

print(variable1)
print(variable2)

print()

print('Ej.2 - intercambio de valores con variable auxiliar')
variable1 = 1
variable2 = 2

auxiliar = variable1
variable1 = variable2
variable2 = auxiliar

print(variable1)
print(variable2)

print()

print('Ej.3 - forma optima de Python')

variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1

print(variable1)
print(variable2)

print()

# listas en acción intercambiar elementos

print('Ej.1 - intercambiar elementos')

miLista = [1, 2, 3, 4, 5]
print(miLista)

miLista[0], miLista[4] = miLista[4], miLista[0]
miLista[1], miLista[3] = miLista[3], miLista[1]

print(miLista)

print()

print('Ej.2 - intercambiar elementos con for en una lista')

miLista = [1, 2, 3, 4, 5, 6, 7]
longitud = len(miLista)
print(miLista)

for i in range(longitud // 2):
    miLista[i], miLista[longitud -i -1] = miLista[longitud -i -1], miLista[i]

print(miLista)
