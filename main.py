from inventory.manager import InventoryManager
from utils.display import display_menu

def main():
    inventory = InventoryManager()

    while True:
        inventory.display_products()
        display_menu()
        choice = input("Elija opción: ").strip()

        if choice == '1':
            inventory.add_product()
        elif choice == '2':
            inventory.delete_product()
        elif choice == '3':
            inventory.update_product()
        elif choice == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

