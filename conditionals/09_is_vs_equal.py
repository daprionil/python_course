# Cuál es la diferencia entre "==" e "is".
# "==" compara los valores e "is" compara que la variable sea o tenga la misma dirección en memoria

# Con ==

# print(5 == 5)  # True
# print(True == 1)

# Un valor Falsy comparado con un valor Truthy

# print("" == 1)
# print([] == 1)
# print(10 == 10.0) # Funciona con números de diferente tipo también

# Con is

new_list = {"1": "hola"}
other_list = {"1": "hola"}

# print(new_list == other_list)  # True
print(new_list is other_list)  # False, están en diferentes instancias de la memoria
