# Estructura de datos
# Una estructura de datos es un contenedor que almacena valores de forma particular
# y permiten que la información sea accesible de una manera más eficiente, claro está,
# según el problema


# Listas

# Es una estructura de dato que permite almacenar una serie de elementos
# En python las listas son iterables y son mutables
# Esta se define con corchetes ([Any])
# "list" es una palabra reservada


from typing import Any

list_numbers: list[int] = [1, 2, 3, 4, 5]  # Lista de números
list_letters: list[str] = ["a", "b", "c", "d", "e"]  # Lista de letras
list_mixed: list[Any] = [1, "s", [1, 2, 3], 10.2]  # Cualquier tipo de dato

# Ejemplo de la real life

shopping_cart = [1, 2, 3, 4, 5]
print(type(list_mixed))
