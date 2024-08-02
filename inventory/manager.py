from .products import Products
from .prices import Prices
from .stock import Stock

class InventoryManager:
    """Class to manage the inventory of products."""

    def __init__(self):
        """Initialize the inventory with predefined products, prices, and stock."""
        self.products = Products()
        self.prices = Prices()
        self.stock = Stock()

    def display_products(self):
        """Display the list of products with their prices and stock."""
        print("========================================")
        print("Lista de Productos:")
        print("========================================")
        for key in self.products.data:
            print(f"{key} \t {self.products.data[key]} \t {self.prices.data[key]} \t {self.stock.data[key]}")
        print("========================================")

    def add_product(self):
        """Add a new product to the inventory."""
        try:
            new_id = max(self.products.data.keys()) + 1
            name = input("Ingrese el nombre del producto: ").strip()
            price = float(input("Ingrese el precio del producto: ").strip())
            stock = int(input("Ingrese el stock del producto: ").strip())

            if not name or price <= 0 or stock < 0:
                print("Datos inválidos. Intente nuevamente.")
                return

            self.products.data[new_id] = name
            self.prices.data[new_id] = price
            self.stock.data[new_id] = stock
            print(f"Producto '{name}' agregado con éxito.")
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar datos correctos.")

    def delete_product(self):
        """Delete a product from the inventory."""
        self.display_products()
        try:
            product_id = int(input("Ingrese el ID del producto que desea eliminar: ").strip())

            if product_id in self.products.data:
                del self.products.data[product_id]
                del self.prices.data[product_id]
                del self.stock.data[product_id]
                print(f"Producto con ID {product_id} eliminado con éxito.")
            else:
                print("ID de producto no encontrado.")
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar un ID numérico.")

    def update_product(self):
        """Update the details of an existing product."""
        self.display_products()
        try:
            product_id = int(input("Ingrese el ID del producto que desea actualizar: ").strip())

            if product_id in self.products.data:
                name = input(f"Ingrese el nuevo nombre del producto (actual: {self.products.data[product_id]}): ").strip()
                price = float(input(f"Ingrese el nuevo precio del producto (actual: {self.prices.data[product_id]}): ").strip())
                stock = int(input(f"Ingrese el nuevo stock del producto (actual: {self.stock.data[product_id]}): ").strip())

                if not name or price <= 0 or stock < 0:
                    print("Datos inválidos. Intente nuevamente.")
                    return

                self.products.data[product_id] = name
                self.prices.data[product_id] = price
                self.stock.data[product_id] = stock
                print(f"Producto con ID {product_id} actualizado con éxito.")
            else:
                print("ID de producto no encontrado.")
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar datos correctos.")

