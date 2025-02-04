# Estrucuras Condicionales
# uso de if-else

print('Ej.2')
prueba = 1

if prueba == 1:
    print('es igual a 1')
    print('y si es igual')
else:
    print('no es igual a 1')

print()

print('Ej.2b')
x = -5

if x > 0:
    print('x es mayor que cero')
else:
    print('x es menor o igual a cero')

print()

print('Ej.2c')
edad = 17
if edad >= 18 and edad <= 25:
    print('Estas en una edad joven')
    print('Disfruta de tu juventud')
else:
    print('Eres muy joven o demasiado adulto ya')
    print('Disfruta de tu niñez o de tu vejez')
    print('Aprovecha la vida.')

print()

print('Ej.2d')
x = 60

if x % 2 == 0:
    print(x, 'es par')
else:
    print(x, 'es impar')
