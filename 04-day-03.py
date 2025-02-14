# alias en las listas

print('Ej.1 - alias')

a = [1, 2, 3]
b = a

print('Lista a:', a)
print('Lista b:', b)

print(id(a))
print(id(b))

b[0] = 5

print('Lista a:', a)
print('Lista b:', b)

print(id(a))
print(id(b))

