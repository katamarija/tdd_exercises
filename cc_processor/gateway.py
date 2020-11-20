from merchant import Merchant
from customer import Customer

class Gateway:
    def __init__(self):
        self._merchants = {}

    def create_merchant(self, merchant_name):
        merchant = Merchant(merchant_name)
        self._merchants[merchant_name] = merchant
        return merchant

    # Assumption now: always adding a new customer to merchant association and that the customer does not already exist
    def merchant_add_customer(self, merchant_name, customer_name):
        merchant = self.get_merchant(merchant_name)
        customer = Customer(name=customer_name)
        merchant.add_customer(customer)
        return True

    def get_merchant(self, merchant_name):
        return self._merchants[merchant_name]
