# listas tridimensionales

# Ej.1 - hotel

"""
3 edidicios
15 niveles por edificio
20 habitaciones por nivel
300 habitaciones por edificio
900 habitaciones por el hotel completo
false para representar vacias las habitaciones
"""

# creamos las habitaciones del hotel completo
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

"""
El primer indice (0 a 2) selecciona uno de los edificios;
el segundo indice (0 a 14) selecciona el nivel del edificio;
el tercer indice (0 a 19) selecciona el número de habitación;
inicialmente están desocupadas con valor False.
"""

# print(rooms)

""" 
Reservemos una habitación para dos recien casados,
en el segundo edificio, en el decimo piso, habitación 14.
"""
rooms[1][9][13] = True

# print(rooms)

if rooms[1][9][13] == True:
    print('Habitación Ocupada')
else:
    print('Habitación disponible')

"""
asumir la habitación como ocupada = True
desocupar la segunda habitación en el quinto nivel
ubicado en el primer edificio.
"""
rooms[0][4][1] = False


"""
verificar si hay disponibilidad en el nivel 15
del tercer edificio.
"""
rooms[2][14][0] = True  # ocupemos una habitación
rooms[2][14][10] = True
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print('cantidad de habitaciones disponibles')
print('en el tercer edificio, nivel 15 hay')
print('habitaciones disponibles:', vacancy)

