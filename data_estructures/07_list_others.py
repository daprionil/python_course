# Esto no es práctico
numbers = [1, 2, 3, 4, 5]
numbers.append(1)
numbers.append(2)
numbers.append(3)

print(numbers)


# Range - permite crea un objeto de rango de números
numbers_range = list(range(100))
print(numbers_range)


# join - Método de strings que permite juntar (con base en una lista) muchos strings en uno
sentence = "".join(["hola  |", "   | mundo"])
print(sentence)

# sum() - Método global que recibe una lista de números y los suma
total = sum(numbers_range)
maximum = max(numbers_range)
minimum = min(numbers_range)
n_elements = len(numbers_range)
print(
    {
        "total": total,
        "maximum": maximum,
        "minimum": minimum,
        "n_elements": n_elements,
    }
)
