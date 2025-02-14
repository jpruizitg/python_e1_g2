# listas continuación

print('Ej.2 - clonacion')

a = [1, 2, 3]
b = a[:]
c = a.copy()

print('lista a:', a)
print('lista b:', b)
print()
print(id(a))
print(id(b))

print()

b[0] = 5

print('lista a:', a)
print('lista b:', b)
print()
print(id(a))
print(id(b))

print()

# rebanadas o segmentos de listas
print('Ej.3')

my_list = [10, 8, 6, 4, 2]

new_list = my_list[1:3]
new_list2 = my_list[3:5]

print(new_list)
print(new_list2)

print()

print('Ej.4 - indices negativos')
my_list = [10, 2, 6, 3, 9]

new_list = my_list[1:-1]

print(new_list)
print(my_list[-1])

print()

print('Ej.5 - otro ejemplo')

my_list = [10, 2, 6, 3, 9]

new_list = my_list[-1:1]

print(new_list)

print()

print('Ej.6')

my_list = [10, 2, 6, 3, 9]

new_list = my_list[:3]

print(new_list)

print()

new_list2 = my_list[2:]

print(new_list2)

print()

print('Ej.7 - uso de del')

my_list = [10, 2, 6, 3, 9]

del my_list[1:3]
print(my_list)

print()

print('Ej.8 uso de del')

my_list = [10, 2, 6, 3, 9]

del my_list[:]
print(my_list)

print()

print('Ej.9 uso de del')
my_list = [10, 2, 6, 3, 9]
del my_list
print(my_list)
