from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount: float):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of ${amount}")

class CryptocurrencyPayment(PaymentStrategy):
    def process_payment(self, amount: float):
        print(f"Processing cryptocurrency payment of ${amount}")

# Context
class PaymentProcessor:
    def __init__(self):
        self._payment_strategy: PaymentStrategy | None = None

    def set_payment_strategy(self, strategy: PaymentStrategy):
        # Clean up previous strategy if needed
        self._payment_strategy = None
        self._payment_strategy = strategy

    def process_payment(self, amount: float):
        if self._payment_strategy is not None:
            self._payment_strategy.process_payment(amount)
        else:
            print("Payment strategy not set.")

# Client code
if __name__ == "__main__":

    processor = PaymentProcessor()

    # Set strategy at runtime
    strategy = CreditCardPayment()
    processor.set_payment_strategy(strategy)

    processor.process_payment(100.0)

    # Change strategy
    strategy = PayPalPayment()
    processor.set_payment_strategy(strategy)

    processor.process_payment(50.0)


