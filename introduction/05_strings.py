# Strings
# Podemos tener strings de una sola linea o formateada

saludo = "Hola! Bienvenido\n"
email = """
subject: Notificación de transferencia
email: example@gmail.com
message: Realizaste una transferencia
"""

# print(saludo)
# print(email)

# Concatenación
# Nos permite juntar strings, pega un string a otro existente en el lado izquierdo

# Forma 1
# Con el símbolo de adición
# print(saludo + email)

# Forma 2
# Formatted Strings
# Nos permite insertar variables dentro de un texto además del texto

full_email = f"{saludo}\n{email}"
