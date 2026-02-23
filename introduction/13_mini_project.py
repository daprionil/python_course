from datetime import date

# Mini proyecto

# Requisitos para: App de registro
# 1. Nombre, año nacimiento, correo y contraseña
# Mostrar en consola los datos del cliente


def get_input_number(msg: str) -> int:
    isnt_int = True
    value = 0
    while isnt_int:
        try:
            value = int(input(msg))
            isnt_int = False
        except:
            print("El valor es incorrecto, inténtalo nuevamente")

    return value


"""
Nombre: asdas
Email: dasdas@asdas.com
Tendrás 55 años en el 2050
Tu contraseña es: ****
"""


def get_year_date() -> int:
    CURRENT_YEAR = date.today().year
    is_valid_year = False
    year = 0
    while not is_valid_year:
        year = get_input_number("Año de nacimiento:")
        if year > CURRENT_YEAR:
            print("Debes de ingresar un año válido")
            continue
        is_valid_year = True

    return year


name: str = input("Nombre: ")
born_day: int = get_year_date()
email: str = input("Correo electrónico: ")
password: str = input("Contraseña: ")


print(
    f"""
        Nombre: {name}
        Email: {email}
        Tendrás {2050 - born_day} años en el 2050
        Tu contraseña es: {"*" * len(password)}
  """
)
