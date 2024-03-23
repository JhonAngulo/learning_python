name = "Jhon"
last_name = "Angulo"

print(name)
print(last_name)

full_name = name + " " +  last_name
print(full_name)

qoute = "I'm Jhon"
print(qoute)

qoute2 = 'She said "Hello"'
print(qoute2)

# format

template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template)

age = 33
template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y tengo {age} años"
print(template)