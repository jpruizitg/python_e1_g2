# Esctucturas Condicionales

# Ej.1 - uso de if
print('Ej.1')
x = -6

if x > 0:
    print('x es positivo')
print('Aquí continua el programa')

print()

# Ej.1b - Uso de if
print('Ej.1b')
edad = 16

if edad >= 18:
    print('Eres mayor de edad')
    print('pasa adelante')
print('El programa siempre pasa por aquí')

print()

# Ej.1c
print('Ej.1c')
usuario = 'admin2'
password = 'secreta123'

if usuario == 'admin' and password == 'secreta123':
    print('Bienvenid@ a nuestro programa')
    print('Ahora puedes usar nuestra solución')
print('el programa siempre pasa por aquí')

print()

# Ej.1d
print('Ej.1d')
sueldo = 12000
tipoCliente = 'A'
saldoMin = 500
mora = 5  # representa en días de atraso

if (sueldo >= 10000 and tipoCliente == 'A') and (saldoMin >= 1000 or mora >= 3):
    print('Tarjeta habiente apto a nueva tarjeta de crédito')
    print('Debes llamar al tarjeta habiente, para indicarle el proceso')
    print('Solicitar lugar de entrega')

print('Tarjeta habiente no apto a tarteja de crédito.')  
# print('Gracias por usar nuestras soluciones de Software')

print()

# Ej.1e
print('Ej.1e')

bandera = False

if not bandera:
    print('Dime que fue verdadera')

print('fin de uso de if')
