# utilizando el operador de igualdad de comparación ==
print(10 == 10)


# otra forma con variables
x = 25
y = 10
print(x == y)


# ejemplo con cadena
cad1 = 'Hola'
cad2 = 'hola'
print(cad1 == cad2)


# asignando a una varibale la comparación
valor1 = 235
valor2 = 235.1
bandera = valor1 == valor2
print(bandera)

print()


# Operador no es igual a (!=)
variable = 5
print(variable != 10)

nota = 25
print(nota != 15)

print()

# operador de comparación mayor y mayor o igual que
print(25 > 10)
print(12 > 55)

a = 36
b = 64
c = a > b
print(c)

salarioAnterior = 2000
salarioActual = 3000

print(salarioAnterior >= salarioActual)

print()

dat1 = 1000
dat2 = 1000
respuesta = dat1 >= dat2
print(respuesta)

print()

# operador de comparación menor o menor igual que
print(15 < 25)
print(36 < 10)

dat1 = 365
dat2 = 660
resDatos = dat1 < dat2
print(resDatos)

print()

edadMin = 18
print(edadMin <= 18)

print(360 <= 525)
print(15 <= 15)

print()

# Determinar mayor y menor en caracteres
# hacer uso de tabla ASCII para determinar valores
print('a' > 'b')
print('z' < 'e')

print()

palabra1 = 'Arbol'
palabra2 = 'arbol'
print(palabra1 > palabra2)
print(palabra1 < palabra2)

word1 = "zorro"
word2 = "Zorros"
print(word1 > word2)

pal1 = 'ARBOLES'
pal2 = 'arbol'
print(pal2 < pal1)

print()

# uso de operadores Booleanos not, and, or
print(not 50 > 10)
print(not "casa" == "carro")

print()

print(25 > 10 and 50 < 100)  # T
print(150 == 100 and 65 > 25)  # F

print()

sueldo = 5000
edad = 25
print(sueldo <= 3000 or edad >= 18)  # T

# and es verdadera si ambos son verdaderos de ahi todas son falsas
# or es falso si ambos son falsos de ahi todas son verdaderas

