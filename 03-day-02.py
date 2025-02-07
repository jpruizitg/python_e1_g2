# funciones max() y min()

# solicitar 3 números al usuario
number1 = int(input('Ingresa el primer numero: '))
number2 = int(input('Ingresa el segundo numero: '))
number3 = int(input('Ingresa el tercer numero: '))

maxNumber = max(number1, number2, number3)
print('El numero mayor es:', maxNumber)

print()

minNumber = min(number1, number2, number3)
print('El numero menor es:', minNumber)

print()

print(max(44, 2, 100, 88))