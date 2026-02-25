import os
import time


# Carrito de compras que
class ShoppingCart:
    shopping_cart_elements: list[dict[str, int | str]]
    my_shopping_cart: list[dict[str, int | str]]

    def __init__(self) -> None:
        self.my_shopping_cart = []

    def run(self):
        self.show_menu()

    def add_product(self):
        self.clean_screen()
        self.print_display("###### Agregando elemento al carrito ######")

        # Nombre
        name = self.input_display("Nombre: ")

        # Precio
        price = self.input_display("Precio: ")

        # Hallar el id máximo y asignarlo con +1
        list_ids = [p["value"] for p in self.my_shopping_cart] or [0]
        new_cart_id = int(max(list_ids)) + 1

        self.my_shopping_cart.append(
            {"label": name, "value": new_cart_id, "price": price}
        )
        self.print_display("Producto creado correctamente")
        self.back_to_menu()

    def remove_product(self):
        self.clean_screen()
        self.display_shopping_cart(False)

        # id de producto
        try:
            product_id = int(
                self.input_display("Ingresa el id del producto a eliminar: ")
            )
            product = [
                product
                for product in self.my_shopping_cart
                if product.__getitem__("value") == product_id
            ]
            if len(product) == 0:
                raise Exception("El producto no existe")

            # eliminarlo del carrito
            position_product = self.my_shopping_cart.index(product[0])
            self.my_shopping_cart.pop(position_product)
            self.print_display(
                f"El producto {product.__getitem__(0).__getitem__('label')} se ha eliminado"
            )
        except Exception:
            self.print_display("El id del producto es incorrecto")

        self.back_to_menu()

    def display_shopping_cart(self, go_to_menu: bool = True):
        self.clean_screen()

        self.print_display("###### Tu carrito de compras ######")

        # tomar la lista de agregados y mostrarla
        if len(self.my_shopping_cart) == 0:
            self.print_display("No existen productos por mostrar")
        else:
            items_text: list[str] = []
            for product in self.my_shopping_cart:
                items_text.append(
                    f"{product.__getitem__('label')} | {product.__getitem__('price')} | Id: {product.__getitem__('value')}\n"
                )
            self.print_display("".join(items_text))

        self.input_display("(Enter para continuar...)")

        if go_to_menu:
            self.back_to_menu()

    def show_menu(self):
        self.clean_screen()
        menu = """
        Carrito de compras

        1. Agregar producto
        2. Eliminar productos
        3. Ver productos disponibles
        4. Buscar producto
        5. Total productos del carrito
        6. Vaciar el carrito

        Elige una opción (1-6):
        """
        option_selected = int(self.input_display(menu))
        # Opción para añadir
        if option_selected == 1:
            self.add_product()
        elif option_selected == 2:
            self.remove_product()
        elif option_selected == 3:
            self.display_shopping_cart()
        elif option_selected == 4:
            self.search_product()
        elif option_selected == 5:
            self.count_cart()
        elif option_selected == 6:
            self.clear_cart()

    def count_cart(self):
        self.clean_screen()

        self.print_display(
            f"Tienes {len(self.my_shopping_cart)} productos en el carrito"
        )

        self.input_display("(Enter para continuar)...")

        self.back_to_menu()

    def search_product(self):
        self.clean_screen()

        # Recibe el nombre
        name_to_search = self.input_display("Escribe el nombre del producto: ")

        # Busca el producto en el carrito
        product_found = None
        for product in self.my_shopping_cart:
            if name_to_search.lower() in str(product["label"]).lower():
                product_found = product

        # Lo muestra si lo encuentra
        if product_found:
            text = f"id: {product_found['value']} | {product_found['label']} | ${product_found['price']}"
            self.print_display(text)
        else:
            # Si no lo encuentra un error
            self.print_display(f"El producto [{name_to_search}] no fue encontrado")

        self.back_to_menu()

    def clear_cart(self):
        self.clean_screen()

        # Limpiar carrito
        self.my_shopping_cart.clear()
        self.print_display("Carrito limpiado")
        self.back_to_menu()

    def print_display(self, data: str):
        print(f"""
        {data}""")

    def input_display(self, data: str) -> str:
        return input(
            f"""
        {data}"""
        )

    def clean_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def back_to_menu(self):
        time.sleep(2)
        self.clean_screen()
        self.show_menu()


app = ShoppingCart()
app.run()
