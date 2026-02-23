# list slicing
shopping_cart = ["Camisa", "Zapatos", "Medias"]
# print(shopping_cart[1]) # Zapatos

# Cortar listas o Extraer una parte
# print(shopping_cart[1:])  # Se manipula el valor pero no reasigna la variable

# Mutar la lista
shopping_cart[1] = "Tenis"
# print(shopping_cart)

new_cart = shopping_cart[
    :
]  # Crea una nueva lista en lugar de copiar la dirección en memoria
print(new_cart is shopping_cart)
