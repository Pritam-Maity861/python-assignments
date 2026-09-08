"""
Assigment 1:  A solid example of abstract class with code 
"""

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    def __init__(self, merchant_id):
        self.merchant_id = merchant_id

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def process_payment(self, amount, currency="USD"):
        pass

    def generate_receipt(self, transaction_id, amount, currency):
        print(f"Receipt [{transaction_id}]: Charged {amount} {currency} via Merchant ID: {self.merchant_id}")


class StripeGateway(PaymentGateway):
    def authenticate(self):
        print(f"Authenticating Stripe merchant: {self.merchant_id}")
        return True

    def process_payment(self, amount, currency="USD"):
        self.authenticate()
        tx_id = f"st_tx_{int(amount*100)}"
        print(f"Processing ${amount:.2f} transaction on Stripe...")
        self.generate_receipt(tx_id, amount, currency)
        return tx_id


class PayPalGateway(PaymentGateway):
    def authenticate(self):
        print(f"Authenticating PayPal merchant account: {self.merchant_id}")
        return True

    def process_payment(self, amount, currency="USD"):
        self.authenticate()
        tx_id = f"pp_tx_{int(amount*100)}"
        print(f"Executing PayPal checkout for ${amount:.2f}...")
        self.generate_receipt(tx_id, amount, currency)
        return tx_id


def process_checkout(gateway: PaymentGateway, amount: float):
    return gateway.process_payment(amount)


if __name__ == "__main__":
    try:
        base_gateway = PaymentGateway("merch_test")
    except TypeError as e:
        print(f"Expected Error: Cannot instantiate abstract class directly -> {e}\n")

    stripe = StripeGateway("stripe_merch_9901")
    paypal = PayPalGateway("paypal_merch_4412")

    process_checkout(stripe, 150.00)
    print("-" * 40)
    process_checkout(paypal, 85.50)
