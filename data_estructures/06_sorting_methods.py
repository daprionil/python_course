# Métodos de ordenamiento
letters = [
    "k",
    "l",
    "j",
    "a",
    "s",
    "l",
    "k",
    "d",
    "n",
    "a",
    "k",
    "s",
    "d",
    "k",
    "l",
    "j",
    "c",
    "j",
    "v",
    "n",
    "d",
    "m",
    "s",
    "s",
    "a",
]
# sort - ordena de menor a mayor o en orden alfabético las letras modificando la lista original
# letters.sort()

print(letters)  # Aquí ya ha sido modificada

# sorted - Recibe un iterable y retorna una lista ordenada sin modificar la original
new_letters = sorted(letters)

# Copy - Otra forma de copiar una lista | Es un método interno de las listas
new_letters_2 = letters.copy()

# Reverse - Voltea la lista pero modificando la lista original
new_letters_2.reverse()
