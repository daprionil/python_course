# Control de flujo
# Hace referencia al flujo de validaciones que se hacen para lograr una funcionalidad
# Es mantener las coherencia de lo que esperamos con todos los casos posibles dentro de la lógica
# a través de validaciones


edad = int(input("Introduce tu edad: "))

if edad <= 0:
    print("No es una edad válida")
elif edad <= 12:
    print("Eres un niño")
elif edad < 17:
    print("You are a teenager")
elif edad <= 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
