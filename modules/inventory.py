# inventory.py

import map


class Inventory:

    def __init__(self):
        self.items = {}

    def add_item(self, item, amount=1):

        if item in self.items:
            self.items[item] += amount
        else:
            self.items[item] = amount

        print(f"{amount}x {item} added!")

    def remove_item(self, item, amount=1):

        if item not in self.items:
            print("Item not found.")
            return

        self.items[item] -= amount

        if self.items[item] <= 0:
            del self.items[item]

        print(f"{amount}x {item} removed!")

    def view_inventory(self):

        print("\n- INVENTORY")

        if not self.items:
            print("Inventory is empty.\n")
            return

        for item, amount in self.items.items():
            print(f"{item}: {amount}")

        print()


# attach inventory to player
map.steve.inventory = Inventory()


def inventory_menu():

    while True:

        choice = input(
            "Inventory Menu\n"
            "(view/add/remove/exit)\n"
        )

        if choice == "view":
            map.steve.inventory.view_inventory()

        elif choice == "add":

            item = input("Item name: ")
            amount = int(input("Amount: "))

            map.steve.inventory.add_item(item, amount)

        elif choice == "remove":

            item = input("Item name: ")
            amount = int(input("Amount: "))

            map.steve.inventory.remove_item(item, amount)

        elif choice == "exit":
            break

        else:
            print("Invalid option.")