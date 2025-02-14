# extras de listas

list = [3, 1, 4, 2, 5]

list.sort(reverse=True)
print(list)

print('-----')

numEnt = [1, 2, 3, 4, 5]
numeros_invertidos = numEnt[::-1]
print(numeros_invertidos)

print('-----')

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista_completa = lista1 + lista2

print(lista_completa)

print('-----')

repetecion = 3
numeros =[0] * repetecion
print(numeros)

print('-----')

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_combinada = [*lista1, *lista2]
print(lista_combinada)

print('-----')

listaNew = [1, 2, 3, 2, 4, 1, 5]
lista_sin_duplicados = list(dict.fromkeys(listaNew))
print(lista_sin_duplicados)

print('-----')

n = 5
lista_consecutiva = list(range(1, n + 1))
print(lista_consecutiva)

print('-----')

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combinacion = [(x, y) for x in list1 for y in list2]
print(combinacion)

print('-----')

listaCadena = ['1', '2', '3', '4', '5']
listaEnteros = [int(x) for x in listaCadena]
print(listaEnteros)
print(type(listaCadena))
print(type(listaEnteros))

print('-----')

oraciones = ['Hola mundo', 'Python es genial', 'listas por comprension son poderosas']
palabras = [palabra for oracion in oraciones for palabra in oracion.split()]
print(palabras)

