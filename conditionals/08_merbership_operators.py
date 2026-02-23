# Operadores de pertenencia
# Estos operadores nos permite conocer si un valor se encuentra o no dentro de una lista o string

# in

print(9 in range(1, 10))  # True
print(11 in range(1, 10))  # False
print(10 in range(1, 10))  # False

fruits = ["coco", "banano", "fresa", "mamoncillo"]
print("fresa" in fruits)  # True

# not in
print(10 not in range(1, 10))  # True

print(4 in {1, 2, 3})  # en Set también funciona
print(1 in (1, 2, 3))  # En una tupla
print(type({1, 2, 3}))

print("a" in "Programador")
