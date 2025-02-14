# funciones parametrizadas

print('Ej.1')

def message(number):
    print('El numero es:', number)


message(5)

print()

print('Ej.2')

def message2(number):
    print('El numero es:', number)


number = 1234
message2(10)
print(number)

print()

print('Ej.3')

def mensaje(what, number):
    print('Ingresa', what, 'Numero', number)


# invocar
mensaje('telefono', 10)
mensaje('precio', 5.50)
mensaje('numero', 'numero')

print()

print('Ej.4')

def miFuncion(parametro1, parametro2):
    print(parametro1, parametro2)
    print(parametro1 + parametro2)


argumento1 = 10
argumento2 = 25.5

miFuncion(argumento1, argumento2)

print()

print('Ej.5')

def promedio(x, y, z):
    prom = (x + y + z) / 3
    print('El promedio es:', prom)


num1 = int(input('Primer numero: '))
num2 = int(input('Segundo numero: '))
num3 = int(input('Tercer numero: '))

promedio(num1, num2, num3)

