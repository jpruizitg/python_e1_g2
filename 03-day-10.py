# listas - continuación

# Ej.18 - reccoriendo una lista con for
colores = ['rojo', 'negro', 'verde']

for color in colores:
    print('El color es:', color)

print()

# Ej.19 - recorriendo una lista con while
animales = ['aves', 'reptiles', 'anfibios', 'salvajes']

i = 0
while i < 4:
    print(animales[i])
    i = i + 1

print()

# Ej.20 - recorriendo una lista con while y len()
utEscolares = ['lapiz', 'crayon', 'regla', 'marcador', 'lapicero']

i = 0
while i < len(utEscolares):
    print('El util escolar es:', utEscolares[i])
    i = i + 1

print()

# Ej.21 - Sumar los elementos en una lista
listaSumar = [25, 10, 5, 15, 1]

total = 0

for i in range(len(listaSumar)):
    total += listaSumar[i]

print('total es:', total)

print()

# Ej.22 - otra manera de resolver el anterior
listaSumar2 = [25, 10, 5, 15, 1]
total = 0

for i in listaSumar2:
    total += i

print('el total es:', total)