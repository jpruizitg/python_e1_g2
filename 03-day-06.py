# break y continue

print('Ej.1 - break')

for i in range(1, 6):
    if i == 3:
        break
    print('Dentro del bucle.', i)

print('Fuera del bucle.')

print()

print('Ej.2 - continue')

for i in range(1, 6):
    if i == 3:
        continue
    print('Dentro del bucle.', i)

print('fuera del bucle')

print()

print('Ej.3 - continue')
print('un bucle para saltar los numeros pares')

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

print()


print('Ej.4 - break')

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

for numero in numeros:
    if numero == 6:
        print('se encontro el numero 6')
        break
    print(numero)

