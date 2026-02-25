# Métodos de ordenamiento
# Nos ayudan a buscar elementos dentro de una lista
listNumbers = list[int]

letters: listNumbers = [1, 3, 30]
numbers: list[listNumbers | int] = [1, 2, letters, 3, 4, 5]

# index - Retorna el indice de donde se encuentra el valor que le pasamos
# Si no encuentra, genera un error
# print(numbers.index([1, 3, 30]))

# permite buscar entre un rango
# print(numbers.index([1, 3, 30], 1, 3))

# in - Permite buscar un valor dentro de una lista
# Retorna un booleano
# print(4 in numbers)


# Count - Retorna la cantidad de elementos encontrados de la lista
print(numbers.count(2))
