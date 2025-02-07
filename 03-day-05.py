# Ciclos repetitivos continuación

print('Ej.1 - for')

for i in range(10):
    print('El valor de i es actualmente', i)

print()

print('Ej.2')

for i in range(2, 8):
    print('el valor de i es actualmente', i)

print()

print('Ej.3')

mensaje = "Hola Mundo Otra Vez!"

for caracter in mensaje:
    print(caracter)

print()

print('Ej.4')

numeros = 1,2,3,4,5

for numero in numeros:
    print(numero)

print()

print('Ej.5')

for multiplicando in range(1, 11):
    print('Tabla del', multiplicando)
    for multiplicador in range(1, 11):
        resultado = multiplicando * multiplicador
        print(multiplicando, 'x', multiplicador, '=', resultado)
    print()
    
print()

print('Ej.5')

for i in range(0, 11, 2):
    print(i)
