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

    def merchant_charge_customer(self, merchant_name, customer_name, card_type, card_number, charge_amount, spending_limit):
        merchant = self.get_merchant(merchant_name)
        if merchant.get_customer(customer_name) == None:
            self.merchant_add_customer(merchant_name, customer_name)
        customer = merchant.get_customer(customer_name)
        if customer.get_card(card_type) == None:
            customer.add_card(card_type, card_number, spending_limit)
        customer.get_card(card_type).charge(charge_amount)
        return True

