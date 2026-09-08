"""
Assignment 5: Advanced Dataclasses (InitVar, __post_init__, field, Real-world Use Case)
"""

from dataclasses import dataclass, field, InitVar
from typing import List

@dataclass
class OrderInvoice:
    order_id: str
    customer_email: str
    unit_price: float
    quantity: int
    discount_pct: InitVar[float] = 0.0

    tags: List[str] = field(default_factory=list)

    final_price: float = field(init=False)
    tax_amount: float = field(init=False)

    def __post_init__(self, discount_pct: float):
        if self.unit_price <= 0 or self.quantity <= 0:
            raise ValueError("Unit price and quantity must be positive.")

        self.customer_email = self.customer_email.strip().lower()

        subtotal = self.unit_price * self.quantity
        discounted = subtotal * (1 - discount_pct / 100)

        self.tax_amount = round(discounted * 0.18, 2)
        self.final_price = round(discounted + self.tax_amount, 2)


if __name__ == "__main__":
    invoice = OrderInvoice(
        order_id="1",
        customer_email="pritam@gmail.com",
        unit_price=100.0,
        quantity=2,
        discount_pct=10.0,
        tags=["electronics", "priority"]
    )

    print("Order Invoice Object")
    print(f"Order ID: {invoice.order_id}")
    print(f"Cleaned Email: {invoice.customer_email}")
    print(f"Tags: {invoice.tags}")
    print(f"Calculated Tax (18%): ${invoice.tax_amount}")
    print(f"Calculated Final Price: ${invoice.final_price}")

   
