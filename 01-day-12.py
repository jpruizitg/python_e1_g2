print('Variables')

variable = 1
balance_general = 1000.0
nombre_cliente = 'Juan Ruiz'
clasificacion = 'A'
estado = True

print(variable)
print(balance_general)
print(nombre_cliente)
print(clasificacion)
print(estado)

print()
print('Tipos de variables')
print(type(variable))
print(type(balance_general))
print(type(nombre_cliente))
print(type(clasificacion))
print(type(estado))
print()

print('Python dara un error si se usa')
print('una variable que no exista')
var = 1
print(var)
# print(Var)  variable Var no creada
print()

print('Case Sensitive demostracion')
a = 150
A = 100
print(a)
print(A)
print('El saldo pendiente es: ', A)
print()

print('Tipos de Variable')
numEntero = 115
numDecimal = 12.68
varCaracter = "a"
varCadena = 'esto es una cadena'
bandera = True

print('otra forma de asignar variables en Python')
A, B, C = 15, 64.25, 'cadena'
print(A)
print(B)
print(C)

print(type(A))
print(type(B))
print(type(C))

print()
print('Otra forma de desplegar la salida en pantalla')
print(A, B, C)
print()

print('La variable varCadena el valor es:', varCadena)

print()

print('podemos asignar en una linea, un mismo valor')
a = b = c = 'Todas son tipo cadena'
print(a)
print(b)
print(c)

print()

print('podemos realizar calculos con nuestras variables')
numero1 = 66
numero2 = 55
sumNum1Num2 = numero1 + numero2
print('El resultado de sumar numero1 + numero2 es:', sumNum1Num2)

print()

print('Sustituir el valor de una variable')
var1 = 65
print(var1)
var1 = 25.50
print(var1)
var1 = 'cambios'
print(var1)

print()

print('que hara esta salida?')
var = 100
var = 200 + 300
print(var)

print()
print('Realicemos un script para calcular el promedio de 5 notas')
print('de un estudiante, desplegar su nombre y su promedio')
# estudiante = "John Doe"
# nota1 = 3.2
# nota2 = 4.0
# nota3 = 2.5
# nota4 = 3.6
# nota5 = 2.8
# promedio  = (nota1 + nota2 + nota3 + nota4 + nota5)/5.0
# print( "Nota de",estudiante, "es",promedio)

estudiante = "Superman"
nota1 = 35
nota2 = 89
nota3 = 90
nota4 = 55
nota5 = 100
sum_notas = nota1 + nota2 + nota3 + nota4 + nota5

print('opcion 1') 
promedio = sum_notas/5
print("El promedio del ", estudiante, "es: ", promedio)

print('opcion 2')
print('El promedio del alumno', estudiante, ' es: ', (nota1+nota2+nota3+nota4+nota5) / 5)

print()

print('cosas que no podemos hacer con las variables')
varSting = 'Soy una cadena'
varNumero = 25
# print(varSting + varNumero)
print('no son del mismo tipo, no se pueden')
print('concatenar u operar')

# nota1 = input
# nota2 = input
# nota3 = input
# sumnotas = sum(nota1, nota2, nota3)
# promedio = sumnotas/3      

print('ejemplo final con variables')
# 'Me llamo' miNombre 'mi apellido' 'es' miApellido 'tengo' miEdad
# 'y' 'naci en:' pais ' y me dedico a' profesion
mi_nombre = "Juancho"
mi_apellido = "De la Vega"
mi_edad = "83"
pais = "Puerto Rico"
profesion = "dibujar"
print("Mi nombre es",mi_nombre, 'mi apellido es:', mi_apellido, "tengo", mi_edad, "años de edad y nací en",pais,"y me decidico a", profesion)
print()


# nombre = str(input ( cual es tu nombre))
# apellido = str(input ( cual es tu apellido))
# edad = str(input ( cual es tu edad))
# profesion = str(input ( cual es tu profesion)
# pais = str(input ( cual es tu pais))
# print(nombre,apellido, edad, profesion, pais, sep='-')
 
 