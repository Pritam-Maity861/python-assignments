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
class based approach
'''

class ProductNotFoundError(Exception):
    pass

class InvalidStockError(Exception):
    pass

class InsufficientStockError(Exception):
    pass


class Inventory:
    def __init__(self):
        self.inventory = {
            "laptop": 10,
            "mouse": 50,
            "keyboard": 25
        }

    def add_product(self, product, quantity):
        if quantity < 0:
            raise InvalidStockError("Stock quantity cannot be negative.")

        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity

        print(f"{product} added successfully.")

    def remove_product(self, product):
        if product not in self.inventory:
            raise ProductNotFoundError("Product not exist.")

        del self.inventory[product]
        print(f"{product} removed successfully.")

    def sell_product(self, product, quantity):
        if product not in self.inventory:
            raise ProductNotFoundError("Cannot sell a nonexistent product.")

        if quantity <= 0:
            raise InvalidStockError("Quantity must be positive.")

        if quantity > self.inventory[product]:
            raise InsufficientStockError("Cannot sell more than available stock.")

        self.inventory[product] -= quantity
        print(f"Sold {quantity} {product}.")

    def restock_product(self, product, quantity):
        if product not in self.inventory:
            raise ProductNotFoundError("Cannot restock a nonexistent product.")
        if quantity <= 0:
            raise InvalidStockError("Restock quantity must be positive.")

        self.inventory[product] += quantity
        print(f"Restocked {quantity} {product}.")

    def check_stock(self, product):
        if product not in self.inventory:
            raise ProductNotFoundError("Product does not exist.")

        print(f"{product} stock:",self.inventory[product])
        return self.inventory[product]


inventory = Inventory()

try:
    print("Initial inventory:")
    print(inventory.inventory)
    inventory.add_product("monitor", 15)
    inventory.sell_product("laptop", 2)
    inventory.restock_product("mouse", 10)
    inventory.check_stock("laptop")
    inventory.check_stock("mouse")
    print("\nFinal inventory:")
    print(inventory.inventory)
except (
    ProductNotFoundError,
    InvalidStockError,
    InsufficientStockError
) as error:
    print("Error:", error)
