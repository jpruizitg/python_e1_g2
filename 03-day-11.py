# listas continuación ...

# método extend()
num1 = [1, 2, 3]
otros_numeros = [4, 5, 6]
print('num1 es:', num1)
print('otros_numeros es:', otros_numeros)
print()

num1.extend(otros_numeros)
print('num1 es:', num1)
print('otros_numeros es:', otros_numeros)
print()

# método remove()
nombres = ['Juan', 'Omar', 'Claudia']
print(nombres)

nombres.remove('Omar')
print(nombres)

print()

# método pop()
num2 = [1, 2, 3, 4, 5]
print(num2)

elemento_eliminado = num2.pop(2)
print(num2)
print(elemento_eliminado)

print()

# método index()
num3 = [5, 4, 3, 2, 1, 3]
print(num3)

posicion = num3.index(3)
print(posicion)

print()

# método count()
num4 = [10, 3, 5, 3, 20, 15, 3, 8, 3]
cantidad = num4.count(3)
print(cantidad)

print()

# método clear()
num6 = [1, 2, 3]

num6.clear()
print(num6)

print()

del num6
print(num6)

print()


# método zip()
names = ['Juan', 'Maria', 'Carlos']
edades = [30, 50, 25]

for nombre, edad in zip(names, edades):
    print('Nombre:', nombre, 'Edad:', edad)

print()

