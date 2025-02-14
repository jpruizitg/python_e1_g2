# ejercicios de funciones
print('Ej.1')

def menu():
    print('Bienvenido a nuestro Menu')
    print('Elija una opcion:')
    print('--------------------------')
    print('1) Opcion')
    print('2) Opcion')
    print('3) Opcion')
    print('3) Salir')
    print()


print('Podemos utilziar el menu multiples veces.')
menu()
print('Podemos volver a utilizar el menu')
menu()

print('-' * 5)

def suma():
    a = 10
    b = 25
    c = a + b
    print('la suma es:', c)


suma()

print('-' * 5)

print('Ej.3')

def suma2():
    print('Funcion suma de dos numeros')
    a = int(input('Ingresa numero 1: '))
    b = int(input('Ingresa numero 2: '))
    c = a + b
    print('la suma es:', c)


suma2()
print()
suma2()
