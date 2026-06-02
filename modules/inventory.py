from modules.player import Player
import tabulate


class Inventory:
    
    def __init__(self, name, inventory: int = 3):
        self.name = name
        self.inventory = [["EMPTY"] for i in range(inventory)]

    def view_inventory(self):
        print("INVENTORY: ")
        print(tabulate.tabulate(self.inventory, tablefmt="fancy_grid"))


class Jacket(Inventory):
    def __init__(self, inventory, player_name: Player):
        super().__init__(inventory)
        self.player_name = player_name


class Chest(Inventory):
    def __init__(self, inventory, location):
        super().__init__(inventory)
        self.location = location