import enum
import os


class Options(enum.Enum):
    ADD_BOOK = 1
    SHOW_BOOKS = 2
    DELETE_BOOK = 3
    SHOW_GENERAL_SUMMARY = 4


class OptionsDescription(enum.Enum):
    ADD_BOOK = "Agregar libro"
    SHOW_BOOKS = "Mostrar libros"
    DELETE_BOOK = "Eliminar libro"
    SHOW_GENERAL_SUMMARY = "Mostrar resumen total"


class MenuApp:
    name: str
    user_email: str
    password: str

    exit_app: str

    option_selected: int

    def __init__(self) -> None:
        # Validaciones iniciales
        self.name = "David"
        self.user_email = "example"
        self.password = "123"
        self.start_app()

    def start_app(self):
        # Pedir nombre e email al usuario
        print("Para iniciar, ingrese sus datos:")

        user_email = input("Email: ")
        password = input("Contraseña: ")

        # Debe iniciar sesión correctamente
        if not (user_email == self.user_email and password == self.password):
            return
        # Si la validación es correcta entonces muestra el menú
        self.show_general_menu()

    def show_general_menu(self):
        self.clean_screen()
        all_menu = ""

        for option in Options:
            all_menu += f"{option.value}: {OptionsDescription[option.name].value}\n"

        print(all_menu)

        self.option_selected = int(input("Ingrese la opción: "))
        self.show_selected_menu()

    def show_selected_menu(self):
        self.clean_screen()

        menus = {Options.ADD_BOOK.value: "hola"}
        menu_selected = menus[self.option_selected]

        print(menu_selected)

    def add_book(self):
        # Nombre, email
        pass

    def clean_screen(self):
        os.system("cls" if os.name == "nt" else "clear")


MenuApp().start_app()
