# Ordenamiento tipo burbuja

print('Ej.1')

my_list = [8, 10, 6, 2, 4]
print(my_list)

for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparación
    if my_list[i] > my_list[i + 1]:  # comparar elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

print()

print('Ej.2 - solucion completa')

my_list = [8, 10, 6, 2, 4, 1]
print(my_list)
swapped = True  # lo necesitamos True para ingresar al bucle while de intercambios

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    
    for i in range(len(my_list) - 1):  
        if my_list[i] > my_list[i + 1]:  # comparar elementos adyacentes
            swapped = True  # Ocurrio el intercambio
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]


print(my_list)

print()

print('Ej.3 - solucion interactiva')

my_list = []
swapped = True

num = int(input('¿Cuantos elementos deseas ordenar?: '))

for i in range(num):
    val = int(input('Ingresa un elemento de la lista: '))
    my_list.append(val)

print('Lista sin ordenar:', my_list)

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    
    for i in range(len(my_list) - 1):  
        if my_list[i] > my_list[i + 1]:  # comparar elementos adyacentes
            swapped = True  # Ocurrio el intercambio
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]


print('Lista ordenada ascendentemente:', my_list)

print()

print('Ej.4 - ordenamineto por metodo sort()')

my_list = [8, 10, 6, 2, 4]
print(my_list)

my_list.sort()

print(my_list)

print()

print('Ej.5 - metodo reverse()')

lst = [5, 3, 1, 2, 4]
print('lista original:', lst)

lst.reverse()

print('lista invertida:', lst)

print()

lst.sort()

print('lista invertida y ordenada:', lst)
