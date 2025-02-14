# listas anidadas

print('Ej.1')
lista = ['hola', 2.0, 5, [10, 20], True]
print(lista)

print(lista[3])
print(lista[3][1])
print(lista[3][0])

print(len(lista))

print()

print('Ej.2 - lista anidada continuacion')

tarjetaHabiente = [['nombre', 'apellido', 47, 'pais', 'direccion', 50266871124],
                   [100000.00, 70000.00, 30000.00, 25000.00, 0.11, 0],
                   [False, 'A']]

print(tarjetaHabiente)

if tarjetaHabiente[1][3]  > 15000.00:
    if tarjetaHabiente[2][0] == True:
        print('Cliente apto a nueva tarjeta')
        print('llamar al cliente, para ofrecer tarjeta nueva')
        print(tarjetaHabiente[0][5])
    else:
        print('TarjetaHabiente no activo')
else:
    print('TarjetaHabiente con sueldo inferior a 15,000')

print()

# Comprensión de listas
print('Ej.3')

numeros = [1, 2, 3, 4, 5]

cuadrados = [numero ** 2 for numero in numeros]

print(cuadrados)

print()

print('Ej.4 - lista a numeros pares')

numeros = [1, 2, 3, 4, 5]

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

print()

print('Ej.5')

nombres = ['Juan', 'Maria', 'Pedro']
apellidos = ['Perez', 'Gomez', 'Gonzalez']

nombres_completos = [nombre + ' ' + apellido for nombre in nombres
                     for apellido in apellidos]

print(nombres_completos)

