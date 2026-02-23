# Variable

# Es un espacio de memoria para almacenar la información
# Cada variable tiene un código ó dirección en la RAM
# Python es un lenguaje interpretado, y este gestiona
# los espacios en memoria; este puede asignar espacios en memoria
# y también puede eliminarlos cuando ya no se usen en el programa


text_to_print = "Saludo"
print(text_to_print)

# Para la creación de variables en python, la convención es snake_case

# Variables privadas (Solo por convención entre desarrolladores)
_text_private = "Privado: "

# Las constantes, por convención deben estar en mayúsculas
YEARS_OLD = 10

print(f"{_text_private} {YEARS_OLD}")
