'''
6. Shopping Cart 
Represent products as: 
products = [ 
{"id": 1, "name": "Laptop", "price": 70000}, 
{"id": 2, "name": "Mouse", "price": 1200}, 
{"id": 3, "name": "Keyboard", "price": 2500}, 
] 
Implement: 
add_to_cart() 
remove_from_cart() 
calculate_subtotal() 
calculate_discount() 
calculate_tax() 
calculate_final_amount() 
Rules 
● Product must exist 
● Quantity must be positive 
● Cannot remove something that isn't in the cart 
● Discount depends on total amount 
Error Handling 
Use exceptions for invalid cases. 
'''

'''
class base approach
'''

class ShoppingCart:
    def __init__(self, products):
        self.products = products
        self.cart = []

    def add_to_cart(self, product_id, quantity):
        if quantity <= 0:
            raise ValueError("quantity must be positive.")

        product = None
        for item in self.products:
            if item["id"] == product_id:
                product = item
                break

        if product is None:
            raise ValueError("Product not exist.")

        for item in self.cart:
            if item["id"] == product_id:
                item["quantity"] += quantity
                print("Product quantity updated.")
                return

        self.cart.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })

        print("Product added to cart successfully.")

    def remove_from_cart(self, product_id):
        for item in self.cart:
            if item["id"] == product_id:
                self.cart.remove(item)
                print("Product removed from cart.")
                return

        raise ValueError("Product is not in the cart.")

    def calculate_subtotal(self):
        subtotal = 0
        for item in self.cart:
            subtotal += item["price"] * item["quantity"]

        return subtotal

    def calculate_discount(self):
        subtotal = self.calculate_subtotal()
        if subtotal >= 10000:
            discount = subtotal * 0.10
        elif subtotal >= 5000:
            discount = subtotal * 0.05
        else:
            discount = 0

        return discount

    def calculate_tax(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        amount_after_discount = subtotal - discount
        tax = amount_after_discount * 0.18

        return tax


    def calculate_final_amount(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        tax = self.calculate_tax()
        final_amount = subtotal - discount + tax

        return final_amount



products = [
    {"id": 1, "name": "Laptop", "price": 70000},
    {"id": 2, "name": "Mouse", "price": 1200},
    {"id": 3, "name": "Keyboard", "price": 2500},
]

cart = ShoppingCart(products)

try:
    cart.add_to_cart(1, 1)
    cart.add_to_cart(2, 2)

    print("\nSubtotal:", cart.calculate_subtotal())
    print("Discount:", cart.calculate_discount())
    print("Tax:", cart.calculate_tax())
    print("Final Amount:", cart.calculate_final_amount())

except ValueError as error:
    print("Error:", error)