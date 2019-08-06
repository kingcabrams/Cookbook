inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    """Print contents and total number of items in inventory."""
    print("Inventory:")
    sum = 0
    for i,j in inventory.items():
        print(j, i)
        sum += j
    print("Total number of items:", sum)


def add_to_inventory(inventory, added_items):
    """Combine a list of loot with an inventory."""
    for i in added_items:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory


display_inventory(inventory)
inventory = add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)
