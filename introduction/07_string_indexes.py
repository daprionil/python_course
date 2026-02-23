# String  indexes
# Un string es una cadena de caracteres
# Cada letra ocupa una posición dentro del string

name = "David"
# print(name[0])  # A través de un índice, podemos acceder a las letras
# print(len(name))  # De esta forma podemos acceder al total de caracteres

# Los índices de acceso a strings, pueden ser positivos o negativos
# print(name[-1])  # De esta forma podemos acceder a la última posición

# [Start:Stop:StepOver]
# Start => Posición inicial
# Final => Posición final
# StepOver => Saltos entre el rango; cada n pasos va a tomar el carácter
# Podemos tomar una parte del string

# print(name[0:5:3])

# ¿Cómo poner el nombre al revés?

print(name[::-1])
