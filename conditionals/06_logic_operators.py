# Operadores lógicos

# and - Todos los valores deben de ser verdaderos

print(True and False)  # False
print(True and True)  # True
print(False and False)  # False
print(False and True)  # False

# or - Al menos un valor verdadero
print(True or False)  # True
print(True or True)  # True
print(False or False)  # False
print(False or True)  # True

# not - Invierta el booleano (Negación)

print(not True)  # False
print(not False)  # True


# Ejemplo práctico con and

age = 25
licensed = True

if age >= 18 and licensed:
    print("Puedes conducir")

# Ejemplo práctico con or

is_student = False
membership = True

if is_student or membership:
    print("Obtienes un descuento especial")

# Ejemplo práctico con not

is_admin = False

if not is_admin:
    print("Acceso denegado")
