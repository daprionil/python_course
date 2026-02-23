# Tipos de Datos

# string - Cadenas de texto
saludo = "Hola!"

# int - Números enteros
years_old = 12

# Float - Números decimales
temp = 23.3

# Booleanos - Verdadero o Falso
is_valid = True

# Estructuras de Datos

# Listas - Una colección de valores
lista = [1, 2, 4]

# Tupla
tuple_value = (1, 2, 3, 1)

# Set

set_list = {1, 2, 4}

# Diccionario

dict_values = {"hello": "hola", "bye": "adiós"}

# ======================

# Todo en python es un objeto:

print(type(tuple_value))
print(tuple_value.count(1))
print(tuple_value[tuple_value.index(2)])

# Cada variable que almacene un valor es un objeto que contiene la clase perteneciente
# a dicho tipo de valor, este nos deja usar métodos propios de cada tipo/estructura de dato.
# Python usa esto tal como un Object Wrapper en Javascript
