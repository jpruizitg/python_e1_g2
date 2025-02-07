# Listas

# Ej.1 - sintaxis de lista
numeros = [10, 5, 7, 2, 1]

# Ej.2 - definiendo listas
string = ['palabra', 'animal', 'cadena']
numEnteros = [17, 123]
numDecimales = [19.63, 25.8, -19.3, 2123223,12]
valBooleanos = [True, False]
listaChar = ['a']
vacia = []

# Ej.3 - lista mixta
listaMixta = ['String', 100, 'c', True, 124.26]

# Ej.4 - print() visualizar las listas
print(string)
print(numEnteros)
print(numDecimales)
print(valBooleanos)
print(listaChar)
print(vacia)

print(type(string))
print(type(valBooleanos))
print(type(listaChar))

# Ej.4 lista mixta - implementación
tarHab = ['Diego', 'Lima', 36, 5000, 2.55, 'A', True]

# Diego - nombre del tarjeta habiente
# Lima - apellido
# 36 - edad
# 5000 - limite de crédito
# 2.55 - porcentaje de interes
# A - tipo de cliente
# True - cliente activo

print()

# Ej.5 - accediendo a la lista
numeros = [17, 100, 25, 'juan']

print(numeros[1])  # 100
print(numeros[0])  # 17
print(numeros[2])  # 25
print(numeros[3])
print(numeros)

print()

# Sustituyendo elementos (mutabilidad de listas)
numeros = [10, 5, 7, 2, 1]
print('lista original:', numeros)

numeros[0] = 111
print('lista nueva:', numeros)

print()

# Ej.7 - copiando el valor de un elemento a otro
numeros = [10, 5, 7, 2, 1]
print('lista original:', numeros)

numeros[1] = numeros[4]
print('lista nueva:', numeros)

print()


# Ej.8 - función len, cuenta los elementos en una lista
listaNew = [25, 18.5, True, False, 'cadena']

print('la longitud de la lista es:', len(listaNew))

cantElelistaNew = len(listaNew)
print(cantElelistaNew)

print()

# Ej.9 - instrucción del para eliminar elementos
autos = ['chevrolet', 'toyota', 'dodge']
print('lista original:', autos)

del autos[1]
print('nueva lista:', autos)

print()

# Ej.10 manejo de indices
numList = [10, 5, 18, 30]

numList[4] = 1  # produce un error.
print(numList)

print()

# Ej.11 - índices negativos
listaNegativos = [114, 224, 343, 75]

print(listaNegativos[-1])
print(listaNegativos[-2])
