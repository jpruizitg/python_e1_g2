# Ciclos repetitivos

# print('Ej.1 - Ciclo while')
# n = 5
# suma = 0
# i = 1

# while i <= n:
#     suma = suma + i
#     i = i + 1
    
# print('La suma de los primeros', n, 'numeros natuales es', suma)

# print()
# print('n es', n)
# print('suma es', suma)
# print('i es', i)

# print()

# print('Ej.2')
# print('Adivine el numero escondido')
# print()

# numeroSecreto = int(input('Ingresa numero a adivinar (entre 1 y 20): '))
# adivinado = False
# intentos = 0

# while not adivinado:
#     intento = int(input('Adivina el numero (entre 1 y 20): '))
#     intentos += 1  # intentos = intentos + 1
    
#     if intento == numeroSecreto:
#         print('Felicidades adivinaste, en', intentos, 'intentos!')
#         adivinado = True
#     elif intento < numeroSecreto:
#         print('El numero secreto es mayor')
#     else:
#         print('El numero secreto es menor')

# print('Gracias por usar nuestro software de diversion')

# print()


print('Ej.3 - while anidados')
print('Tablas de multiplicar del 1 al 10')
i = 1

while i <= 10:
    j = 1
    print('Tabla del', i)
    while j <= 10:
        resultado = i * j
        print(i, 'x', j, '=', resultado)
        j += 1
    print()
    i += 1

print()

print('Ej.4 - piramide de *')

i = 1

while i <= 5:
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1

print()

print('Ej.5 tablero de ajedrez')
tamanio = 8

fila = 0
while fila < tamanio:
    columna = 0
    while columna < tamanio:
        if (fila + columna) % 2 == 0:
            print('□', end=' ')
        else:
            print('■', end=' ')
        columna += 1
    print()
    fila += 1
