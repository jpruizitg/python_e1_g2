# Estructuras condicionales
# uso de if - elif -else
print('Ej.3')

x = 15
y = 15

if x < y:
    print(x, 'es menor que', y)
elif x > y:
    print(x, 'es mayor que', y)
else:
    print(x, '&', y, 'son iguales')
    
print()

print('Ej.3b')
temperatura = float(input('Ingresa temperatura: (rango de 10 a 40): '))

if temperatura <= 10:
    print('Hace mucho frio')
    print('Debes abrigarte, lleva una sudadera')
elif temperatura <= 20:
    print('Hace un poco de frio')
    print('Debes llevar sudadera fresca')
    print('puede que la necesites')
elif temperatura <= 30:
    print('Hace un clima agradable')
    print('No requieres llevar sudadera')
else:
    print('Hace mucho calor')

print()

print('Ej.3c')
numero = int(input('Ingresa un número de -10 a 10: '))

if numero % 2 == 0:
    print('el número es par')
else:
    print('el número es impar')


if numero > 0:
    print('el número es positivo')
elif numero < 0:
    print('el número es negativo')
else:
    print('el número es cero')
