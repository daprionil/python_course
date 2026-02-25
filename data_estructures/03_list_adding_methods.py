# Métodos de adición en listas
numbers = [1, 2, 3, 4, 5]

# Append - Agrega Elementos al final y no retorna nada
numbers.append(200)

# Insert - Agrega un valor en una posición de la lista sin reemplazar el valor existente
# El insert se abre espacio dentro de la lista

numbers.insert(1, 100)

# Extends - Permite insertar una lista a otra al final (mezclar la lista)
numbers.extend([13, 23])
print(numbers)
