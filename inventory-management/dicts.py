"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inv={}
    for item in items:
        count=items.count(item)
        inv.setdefault(item, count)
    return inv
        
def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for item in items:
        if item not in inventory:
            inventory.setdefault(item)
            inventory[item]=1
        else:
            count=inventory[item]
            inventory[item]=count+1
    return inventory
            
def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        list_count=items.count(item)
        dict_count=inventory[item]
        if list_count<=dict_count:
            if item in inventory:
                count=inventory[item]
                inventory[item]=count-1
        else:
            inventory[item]=0
    return inventory
    
def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory:
        inventory.pop(item)
        return inventory
    else:
        return inventory
            
def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    list_inv=[ ]
    for item, item_count in inventory.items():
        if item_count>0:
            list_inv.append((item,item_count))
    return list_inv
            
        
            
            
        
        
