# parámetros posicionales en las funciones

print('Ej.1')

def my_function(a, b, c):
    print(a, b, c)


my_function(1, 2, 3)

my_function(10, 25, 35)

print('---')

print('Ej.2')

def introduction(first_name, last_name):
    print('Hola, mi nombre es:', first_name, last_name)


introduction('Luke', 'Skywalker')
introduction('Jesse','Quick')
introduction('Clark', 'Kent')

print()

print('Presentacion es en Hungria')

introduction('Skywalker', 'Luke')
introduction('Quick', 'Jesse')
introduction('Kent', 'Clark')

print()

# argumento con palabra clave
def introduction2(first_name, last_name):
    print('Hola, mi nombre es:', first_name, last_name)


def introduction3(first_name, last_name):
    print('Hola, mi nombre es:', last_name, first_name)


# introduction2(first_name="James", last_name="Bond")
introduction3(last_name="Stark", first_name="Tony")
introduction3(first_name="Tony", last_name="Stark")

