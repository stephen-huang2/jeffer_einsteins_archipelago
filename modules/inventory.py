import tabulate
from modules.type_write import *

class Inventory:
    
    def __init__(self, name: str, inventory: int = 3):
        self.name = name
        self.inventory = [[f"{i+1}. EMPTY"] for i in range(inventory)]

    def __str__(self):
        return self.name

    def view_inventory(self):
        type_write(f"{self.name}: ")
        print(tabulate.tabulate(self.inventory, tablefmt="fancy_grid"))