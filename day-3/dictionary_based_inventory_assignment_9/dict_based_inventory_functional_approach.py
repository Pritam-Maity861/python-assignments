'''
9. Dictionary-Based Inventory 
Create: 
inventory = { 
"laptop": 10, 
"mouse": 50, 
"keyboard": 25 
} 
Implement: 
add_product() 
remove_product() 
sell_product() 
restock_product() 
check_stock() 
Rules 
● Product cannot have negative stock 
● Cannot sell more than available stock 
● Cannot restock a nonexistent product 
● Cannot sell a nonexistent product 
Use custom exceptions. 
'''

'''
Functional Approach
'''

class ProductNotFoundError(Exception):
    pass

class InvalidStockError(Exception):
    pass

class InsufficientStockError(Exception):
    pass

inventory = {
    "laptop": 10,
    "mouse": 50,
    "keyboard": 25
}


def add_product(product, quantity):
    if quantity < 0:
        raise InvalidStockError("Stock quantity cannot be negative.")
    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity

    print(f"{product} added successfully.")


def remove_product(product):
    if product not in inventory:
        raise ProductNotFoundError("Product does not exist.")
    del inventory[product]
    print(f"{product} removed successfully.")


def sell_product(product, quantity):
    if product not in inventory:
        raise ProductNotFoundError("Cannot sell a nonexistent product.")
    if quantity <= 0:
        raise InvalidStockError("Quantity must be positive.")
    if quantity > inventory[product]:
        raise InsufficientStockError("Cannot sell more than available stock.")
    inventory[product] -= quantity
    print(f"Sold {quantity} {product}.")


def restock_product(product, quantity):
    if product not in inventory:
        raise ProductNotFoundError("Cannot restock a nonexistent product.")
    if quantity <= 0:
        raise InvalidStockError("Restock quantity must be positive.")
    inventory[product] += quantity
    print(f"Restocked {quantity} {product}.")


def check_stock(product):
    if product not in inventory:
        raise ProductNotFoundError("Product does not exist.")
    print(f"{product} stock:", inventory[product])

    return inventory[product]


try:
    print("Initial inventory:")
    print(inventory)
    add_product("monitor", 15)
    sell_product("laptop", 2)
    restock_product("mouse", 10)
    check_stock("laptop")
    check_stock("mouse")
    print("\nFinal inventory:")
    print(inventory)
except (
    ProductNotFoundError,
    InvalidStockError,
    InsufficientStockError
) as error:
    print("Error:", error)
