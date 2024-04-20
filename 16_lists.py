numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(list))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])

text = 'Hola' # los string no se pueden mutar de esta manera, son inmutables
# text[0] = 'W'

tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3])

print(True in types)
print('hola' in types)