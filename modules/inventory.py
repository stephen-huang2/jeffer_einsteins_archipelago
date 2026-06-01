inventory = {}

def add_item(item: str, qty=1):
    """Adds or increases an item's quantity in the inventory."""
    inventory[item] = inventory.get(item, 0) + qty
    print(f"Added {qty}x {item}. Current quantity: {inventory[item]}")

def remove_item(item: str, qty=1):
    if item in inventory:
        if inventory[item] > qty:
            inventory[item] -= qty
            print(f"Removed {qty}x {item}. Remaining: {inventory[item]}")
        else:
            qty_removed = inventory[item]
            del inventory[item]
            print(f"Removed all {qty_removed}x {item} from inventory.")
    else:
        print(f"Error: '{item}' not found in inventory.")

def show_inventory():
    print("\n--- Current Inventory ---")
    if not inventory:
        print("Empty")
    else:
        for item, qty in inventory.items():
            print(f"- {item}: {qty}")
    print("-------------------------\n")

if __name__ == "__main__":
    add_item("wood", 10)
    add_item("Stone", 5)
    add_item("Wood", 5)
    show_inventory()
    
    remove_item("Stone", 2)
    remove_item("water", 2)
    remove_item("Wood", 15)
    show_inventory()