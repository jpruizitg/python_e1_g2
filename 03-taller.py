print("Ejercicio 24")
# monto_final = 0
# salida = False
# print("Ingrese el monto de una venta. (Escriba '0' para finalizar.)")
# while not salida:
#     monto = int(input("Monto de una venta:$"))
#     if monto < 0:
#         print("Monto no válido")
#     elif monto == 0:
#         salida = True
#     else:
#         monto_final += monto
 
# if monto_final > 1000:
#     monto_final = monto_final - (monto_final * .10)
#     print("Monto total a pagar: $", monto_final)
# else:
#     print("Monto total a pagar: $", monto_final)
 
print()

# sumamontos=0
# monto=0
# salir=False
# while not salir:
#     montoentrar=int(input('Entre Monto: '))
#     if montoentrar==0:
#         salir=True
#     else:
#         if montoentrar<0:
#             print('Valor incorrecto')
#         else:
#             sumamontos=sumamontos+montoentrar
# if sumamontos>1000:
#     sumamontos = sumamontos - sumamontos * .10
 
# print('suma montos ',sumamontos)

# print()

# print("Ejercicio 26")
# year = int(input("Entre un año: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Es un año bisiesto")
# else:
#     print("No es un año bisiesto")
   
print()
 
# year = int(input("Entre un año: "))
# if year < 1582:  # Corregido a 1582, año de introducción del calendario gregoriano
#     print('El año no está en el calendario gregoriano')
# elif year % 4 != 0:
#     print('No es bisiesto, no es divisible entre 4')
# elif year % 100 != 0:
#     print('Es bisiesto, es divisible entre 4 pero no entre 100')
# elif year % 400 != 0:
#     print('No es bisiesto, es divisible entre 100 pero no entre 400')
# else:
#     print(year, 'Es bisiesto, es divisible entre 400', sep=': ')
 
 
# print("Ejercicio 29")
# suma_num = 0
# while True:
#     num = int(input('Ingrese un numero entero positivo(para salir, escriba un numero negativo): '))
#     if num < 0:
#         break
#     else:
#         suma_num += num
# print("La suma de los numeros es:", suma_num)
print()
 
# colector = 0
# while 2 > 1:
#     numero = int(input("Ingrese número entero positivo"))
#     colector += numero
#     if numero < 0:
#         break
# print("Gracias",colector )

continuar=True
total=0
while continuar:
    numero=int(input('entre numero:'))
    if numero>0:
       total=total+numero
    else:
     break
   
print(total)
 