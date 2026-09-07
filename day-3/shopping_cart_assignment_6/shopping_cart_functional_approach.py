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
Functional Approach
'''

products = [
    {"id": 1, "name": "Laptop", "price": 70000},
    {"id": 2, "name": "Mouse", "price": 1000},
    {"id": 3, "name": "Keyboard", "price": 1500},
]
cart = []

def add_to_cart(product_id, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")

    product = None
    for item in products:
        if item["id"] == product_id:
            product = item
            break

    if product is None:
        raise ValueError("Product does not exist.")

    for item in cart:
        if item["id"] == product_id:
            item["quantity"] += quantity
            print("Product quantity updated.")
            return

    cart.append({
        "id": product["id"],
        "name": product["name"],
        "price": product["price"],
        "quantity": quantity
    })
    print("Product added to cart.")


def remove_from_cart(product_id):
    for item in cart:
        if item["id"] == product_id:
            cart.remove(item)
            print("Product removed from cart.")
            return

    raise ValueError("Product is not in the cart.")


def calculate_subtotal():
    subtotal = 0
    for item in cart:
        subtotal += item["price"] * item["quantity"]

    return subtotal


def calculate_discount():
    subtotal = calculate_subtotal()
    if subtotal >= 10000:
        discount = subtotal * 0.10
    elif subtotal >= 5000:
        discount = subtotal * 0.05
    else:
        discount = 0

    return discount


def calculate_tax():
    subtotal = calculate_subtotal()
    discount = calculate_discount()
    amount_after_discount = subtotal - discount
    tax = amount_after_discount * 0.18
    return tax


def calculate_final_amount():
    subtotal = calculate_subtotal()
    discount = calculate_discount()
    tax = calculate_tax()
    final_amount = subtotal - discount + tax
    return final_amount


try:
    add_to_cart(1, 1)
    add_to_cart(2, 2)
    print("\n subtotal:", calculate_subtotal())
    print("discount:", calculate_discount())
    print("tax:", calculate_tax())
    print("final amount:", calculate_final_amount())
except ValueError as error:
    print("Error:", error)