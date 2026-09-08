"""
Assignment 3: Dunder Methods and Operator Overloading in Python
"""

class Money:
    def __init__(self, amount: float, currency: str = "USD"):
        self.amount = round(float(amount), 2)
        self.currency = currency.upper()

    def __repr__(self):
        return f"Money(amount={self.amount}, currency='{self.currency}')"

    def __str__(self):
        return f"${self.amount:.2f} {self.currency}"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        if not isinstance(other, Money) or self.currency != other.currency:
            raise TypeError("Cannot compare Money with different currencies or types.")
        return self.amount < other.amount

    def __add__(self, other):
        if not isinstance(other, Money) or self.currency != other.currency:
            raise ValueError("Cannot add Money with different currencies or types.")
        return Money(self.amount + other.amount, self.currency)


class ShoppingCart:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add_item(self, item_name, price: Money):
        self.items.append({"name": item_name, "price": price})

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __repr__(self):
        return f"ShoppingCart(items_count={len(self)})"


if __name__ == "__main__":
    m1 = Money(50.00, "USD")
    m2 = Money(35.50, "USD")
    m3 = Money(50.00, "USD")

    print(f"Str Representation: {m1}")
    print(f"Repr Representation: {repr(m1)}")
    print(f"Equality Check (m1 == m3): {m1 == m3}")
    print(f"Operator Overloading Add (m1 + m2): {m1 + m2}")
    print(f"Operator Overloading Less-Than (m2 < m1): {m2 < m1}")

    cart = ShoppingCart()
    cart.add_item("Python Book", Money(29.99))
    cart.add_item("Wireless Mouse", Money(15.50))

    print("-" * 50)
    print(f"Cart Length (len(cart)): {len(cart)}")
    print(f"Indexing (cart[0]): {cart[0]}")
