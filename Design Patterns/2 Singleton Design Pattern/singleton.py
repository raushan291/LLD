import threading

class PaymentGatewayManager:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        # Prevent re-initialization of the singleton instance
        if PaymentGatewayManager._instance is not None:
            raise Exception("Use get_instance() to get the singleton instance.")
        
        print("Payment Gateway Manager initialized.")
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None: # First check (no locking)
            with cls._lock:  # Thread-safe locking
                if cls._instance is None:  # Second check (with locking)
                    cls._instance = cls()
        return cls._instance
    
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount:.2f} through the Payment Gateway.")


# Client code
if __name__ == "__main__":
    payment_gateway = PaymentGatewayManager.get_instance()
    payment_gateway.process_payment(100.00)

    # Attempt to create another instance (should return the existing instance)
    another_payment_gateway = PaymentGatewayManager.get_instance()

    # Check if both instances are the same.
    if payment_gateway is another_payment_gateway:
        print("Both instances are the same. Singleton pattern is working.")
    else:
        print("Singleton pattern is not working correctly.")