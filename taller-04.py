"""
Ej.1
Lista de Compras: Crea un programa que permita al usuario ingresar 
una lista de compras.
Almacena los elementos en una lista y luego imprime la lista completa.
utilizar la palabra fin para terminar de ingresar las compras.
"""
# salir = False
# art = []
# while salir == False:
#     ar = input("Por favor añada artículo, escriba fin para salir: ")
#     if ar == "fin":
#         salir = True
#     else:
#         art.append(ar)
# print('Lista de compra:',art)  

# flag = True
# lista_compras = []
 
# while flag:
#     elemento = input("Ingrese un articulo para la lista de compras (Escriba 'fin' para finalizar programa y ver la lista): ")
#     if elemento.lower() == "fin":
#         flag = False
#     else:
#         lista_compras.append(elemento)
 
# print("Esta es tu lista de compra:")
# number = 1
# for element in lista_compras:
#     print(number, ".", element, sep="")
#     number += 1


"""
Ej.2
Lista de Nombres: Crea una lista con 5 nombres. 
Pide al usuario que ingrese un nombre. 
Si el nombre ya está en la lista, imprime 
"El nombre ya existe". Si no, agrega el nombre a la lista.
"""
# nombres = ["Jose","Omar","Carlos","Rosaluz","Luis"]
# nuevoNombre = input("Especifique su nombre: ")
# if nuevoNombre in nombres:
#     print("El nombre ya existe no sea tramposo.")
# else:  
#     nombres.append(nuevoNombre)
#     print("Nombre añadido, gracias.")  
# print("Lista de nombres",nombres)


"""
Ej.3
Lista de Contactos: Crea un programa que permita al usuario
ingresar nombres y números de teléfono. 
utilice la palabra fin para dejar de ingresar contactos.
Almacena esta información en una lista de listas (lista bidimensional). 
Luego, permite al usuario buscar un número de teléfono ingresando un nombre.
"""
# contactos = { }
 
# salir = False
# while salir == False:
#     con_nombre = input("Especifique nombre (o escriba fin para salir): ")
#     if con_nombre == "fin":
#         salir = True
#         break
#     else:
#         con_tel = input("Especifique telefono: ")
#         contactos[con_nombre] = {}
#         contactos[con_nombre]["Tel"]   =  con_tel
       
# ruta = input("\nEscriba:\n 1- para ver listado de contactos\n 2- para buscar contacto por nombre")
 
# if ruta == "1":
#     print("Contactos registrados", contactos)
# elif ruta == "2":
#     print(contactos[input("Especifique el nombre a buscar")])

contactos = []

while True:
    nombre = input('Ingrese un nombre (o fin para terminar): ')
    if nombre == 'fin':
        break
    telefono = input('Ingrese un numero de telefono: ')
    contactos.append([nombre, telefono])

nombre_buscar = input('Ingrese un nombre para buscar: ')
for contacto in contactos:
    if contacto[0] == nombre_buscar:
        print('Numero de telefono:', contacto[1])
        break
else:
    print('Nombre no encontrado.')

