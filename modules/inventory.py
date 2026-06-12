import tabulate
from modules.type_write import *


class Inventory:
    """Represents a named inventory with a fixed number of item slots."""

    def __init__(self, name: str, inventory: int = 3):
        self.name = name  # Display name of the inventory
        self.inventory = [[f"{i + 1}. EMPTY"] for i in range(inventory)]  # Initialise slots as EMPTY

    def __str__(self):
        return self.name

    def view_inventory(self):
        """Display the inventory contents as a formatted table."""
        type_write(f"{self.name}: ")
        print(tabulate.tabulate(self.inventory, tablefmt="fancy_grid"))