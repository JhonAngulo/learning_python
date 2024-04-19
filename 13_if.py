if True:
    print('deberia ejecutarse')

if False:
    print('nunca se ejecuta')

# pet = input('¿Cuál es tu mascota favorita? ')

# if pet == 'perro':
#     print('genial tienes buen gusto')

# if pet == 'gato':
#     print('espero tengas suerte')

# if pet == 'pez':
#     print('eres lo maximo')

''' version optimizada '''

pet = input('¿Cuál es tu mascota favorita? ')

if pet == 'perro':
    print('genial tienes buen gusto')
elif pet == 'gato':
    print('espero tengas suerte')
elif pet == 'pez':
    print('eres lo maximo')
else:
    print('no tienes ninguna mascota interesante')

# stock = int(input('Digita el stock '))

# if stock >= 100 and stock <= 1000:
#     print('el stock es correcto')
# else:
#     print('el stock es incorrecto')