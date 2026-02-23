## Input - Entradas por consol
# Permite que la información insertada sea dinámica


def get_age(msg: str) -> int:
    isnt_int = True
    value = 0
    while isnt_int:
        try:
            value = int(input(msg))
            isnt_int = False
        except:
            print("El valor es incorrecto, inténtalo nuevamente")

    return value


name = str(input("Ingresa tu nombre: "))
age = get_age("Ingresa tu edad:")

print(f"\n ########################### \n Nombre: {name} \n Edad: {age}")
