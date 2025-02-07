# Estructuras Condicionales

# Ej.4 - Condicionales anidados
print('Ej.4')
x = 7
y = 7

if x == y:
    print(x, '&', y, 'Son iguales')
else:
    if x < y:
        print(x, 'Es menor que', y)
    else:
        print(x, 'Es mayor que', y)

print()

print('Ej.4b')
nota = 55

if nota >= 60:
    if nota >= 90:
        print('Excelente trabajo')
    elif nota >= 80:
        print('Muy buen trabajo')
    else:
        print('Buen trabajo')
else:
    print('Necesitas mejorar tu aprendizaje')

print()


print('Ej.4c')

edad = int(input('Ingrese su edad: '))
sexo = input('Ingrese su sexo (Masculino o Femenino): ')
sexo_upper = sexo.upper()

if edad >= 18:
    if sexo_upper == 'MASCULINO':
        print('Eres mayor de edad y eres hombre')
    elif sexo_upper == 'FEMENINO':
        print('Eres mayor de edad y eres mujer')
    else:
        print('Eres mayor de edad y tu sexo es desconocido')
else:
    if sexo_upper == 'MASCULINO':
        print('Eres menor de edad y eres un jovencito')
    elif sexo_upper == 'FEMENINO':
        print('Eres menor de edad y eres una jovencita')
    else:
        print('Eres menor de edad y tu sexo es desconocido')


print()

print('Ej.4d')

x = 5
y = 6

if x >= 3:
    if y == 6:
        if (x + y) > 0:
            print('se cumplieron todas las condiciones')
