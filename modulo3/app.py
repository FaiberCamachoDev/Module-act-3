inventory = []
from file import load_csv, save_csv
from services import add_product, show_inventory, show_stats, pp_menu
print("""
-----------------------------------------------
Welcome! let's start to organize your inventory
-----------------------------------------------
""")

def option_menu():
    global inventory
    control_menu = True
    while control_menu:
        pp_menu()
        option = input(">")
        match option:
            case "1":
                add_product(inventory)
            case "2":
                show_inventory(inventory)
            case "3":
                show_stats(inventory)
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                save_csv(inventory)
            case "8":
                load_csv(inventory)
            case "9":
                control_menu = False
            case _:
                print("Insert a valid option")
                continue
option_menu()